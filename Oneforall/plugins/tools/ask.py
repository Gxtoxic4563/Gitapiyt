import os
import time
import httpx
import asyncio
import atexit
from pyrogram import filters
from pyrogram.enums import ChatAction, ChatType
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from motor.motor_asyncio import AsyncIOMotorClient

# Main bot instance import
from Oneforall import app

# =====================================================
# CONFIGURATION & CACHE
# =====================================================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MODEL = "deepseek/deepseek-chat"

BOT_USERNAME = None
BOT_ID = None
USER_COOLDOWN = {} 

# Shared HTTP Client with fine-tuned limits
HTTP = httpx.AsyncClient(
    follow_redirects=True,
    timeout=45.0,
    limits=httpx.Limits(max_keepalive_connections=20, max_connections=50)
)

@atexit.register
def shutdown_http():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(HTTP.aclose())
        else:
            loop.run_until_complete(HTTP.aclose())
    except:
        pass

# =====================================================
# DATABASE SETUP
# =====================================================
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client["ChatBotDB"]
chats_col = db["chats"]

async def is_chatbot_on(chat_id):
    chat = await chats_col.find_one({"chat_id": chat_id})
    return chat.get("status", False) if chat else False

async def toggle_chatbot(chat_id, status):
    await chats_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"status": status}},
        upsert=True
    )

# =====================================================
# OPENROUTER AI ENGINE (ULTRA STABLE)
# =====================================================
async def ask_ai(prompt):
    if not OPENROUTER_API_KEY:
        return "❌ `OPENROUTER_API_KEY` missing!"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/Gxtoxic4563",
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a smart Telegram chatbot. Reply naturally, shortly, and like a real human. Avoid repetitive answers."},
            {"role": "user", "content": prompt},
        ],
    }

    response = None
    for _ in range(2):
        try:
            response = await HTTP.post(url, headers=headers, json=data)
            break
        # Improvement 2: Better timeout coverage (covers all timeout types)
        except httpx.TimeoutException:
            continue

    if not response:
        return "❌ API is not responding after retries."

    try:
        if response.status_code != 200:
            return f"❌ API Error {response.status_code}: {response.text[:200]}"
            
        result = response.json()
        if "choices" not in result:
            return f"⚠️ API logic error: {str(result)}"
            
        reply = result["choices"][0].get("message", {}).get("content", "No reply generated.")
        return reply[:4000]
    except Exception as e:
        return f"❌ System Error: {str(e)}"

# =====================================================
# HELPERS
# =====================================================
async def load_my_data():
    global BOT_USERNAME, BOT_ID
    if BOT_USERNAME is None:
        me = await app.get_me()
        BOT_USERNAME = me.username.lower()
        BOT_ID = me.id

def manage_cooldown(user_id):
    global USER_COOLDOWN
    # Improvement 1: Prevent duplicate cooldown dict growth
    if len(USER_COOLDOWN) > 10000:
        USER_COOLDOWN.clear()
    
    current_time = time.time()
    if current_time - USER_COOLDOWN.get(user_id, 0) < 3:
        return False
    
    USER_COOLDOWN[user_id] = current_time
    return True

# =====================================================
# HANDLERS
# =====================================================

@app.on_message(filters.command("chatbot") & ~filters.edited)
async def chatbot_settings(_, message: Message):
    status = await is_chatbot_on(message.chat.id)
    text = f"🤖 **ChatBot Control Panel**\n\nCurrent Status: {'✅ Enabled' if status else '❌ Disabled'}"
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("Toggle Status", callback_data="toggle_chat")]])
    await message.reply_text(text, reply_markup=buttons)

@app.on_callback_query(filters.regex("toggle_chat"))
async def on_toggle_callback(_, query: CallbackQuery):
    current_status = await is_chatbot_on(query.message.chat.id)
    new_status = not current_status
    await toggle_chatbot(query.message.chat.id, new_status)
    
    status_text = "✅ Enabled" if new_status else "❌ Disabled"
    await query.message.edit_text(
        f"🤖 **ChatBot Control Panel**\n\nCurrent Status: {status_text}",
        reply_markup=query.message.reply_markup
    )
    await query.answer(f"ChatBot {status_text}")

@app.on_message(filters.command("ask") & ~filters.edited)
async def ask_command(_, message: Message):
    if not message.from_user or message.from_user.is_self:
        return

    if not manage_cooldown(message.from_user.id):
        return await message.reply_text("✋ Sabar! 3s cooldown.")

    if len(message.command) < 2:
        return await message.reply_text("Usage: `/ask hello` ")

    query = message.text.split(None, 1)[1]
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = await ask_ai(query)
    await message.reply_text(reply, disable_web_page_preview=True)

@app.on_message(filters.text & ~filters.bot & ~filters.edited)
async def auto_chatbot_handler(_, message: Message):
    global BOT_USERNAME, BOT_ID
    
    if not message.from_user or message.from_user.is_self:
        return
    if not message.text or message.text.startswith(("/", "!")):
        return
    if not await is_chatbot_on(message.chat.id):
        return

    await load_my_data()

    if message.chat.type != ChatType.PRIVATE:
        if message.reply_to_message and message.reply_to_message.from_user:
            if message.reply_to_message.from_user.is_bot and message.reply_to_message.from_user.id != BOT_ID:
                return

        triggered = False
        if message.reply_to_message and message.reply_to_message.from_user:
            if message.reply_to_message.from_user.id == BOT_ID:
                triggered = True
        if f"@{BOT_USERNAME}" in message.text.lower():
            triggered = True
        
        if not triggered:
            return

    if not manage_cooldown(message.from_user.id):
        return

    await app.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = await ask_ai(message.text)
    await message.reply_text(reply, disable_web_page_preview=True)

@app.on_message(filters.sticker & ~filters.bot & ~filters.edited)
async def sticker_reply(_, message: Message):
    if not message.from_user or message.from_user.is_self:
        return
    if await is_chatbot_on(message.chat.id):
        if manage_cooldown(message.from_user.id):
            await message.reply_text("😎 Nice sticker!")
