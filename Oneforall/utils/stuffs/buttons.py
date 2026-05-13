from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle


class BUTTONS(object):

    MBUTTON = [

        # ================= ROW 1 =================

        [
            InlineKeyboardButton(
                "🍭 🤖 ᴄʜᴀᴛɢᴘᴛ",
                callback_data="mplus HELP_ChatGPT",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 📜 ʜɪsᴛᴏʀʏ",
                callback_data="mplus HELP_History",
                style=ButtonStyle.SECONDARY,
            ),

            InlineKeyboardButton(
                "🍭 🎬 ʀᴇᴇʟ",
                callback_data="mplus HELP_Reel",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 2 =================

        [
            InlineKeyboardButton(
                "🍭 📢 ᴛᴀɢ-ᴀʟʟ",
                callback_data="mplus HELP_TagAll",
                style=ButtonStyle.DANGER,
            ),

            InlineKeyboardButton(
                "🍭 ℹ️ ɪɴғᴏ",
                callback_data="mplus HELP_Info",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 ⚙️ ᴇxᴛʀᴀ",
                callback_data="mplus HELP_Extra",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= ROW 3 =================

        [
            InlineKeyboardButton(
                "🍭 💞 ᴄᴏᴜᴘʟᴇs",
                callback_data="mplus HELP_Couples",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 🎭 ᴀᴄᴛɪᴏɴ",
                callback_data="mplus HELP_Action",
                style=ButtonStyle.SECONDARY,
            ),

            InlineKeyboardButton(
                "🍭 🔎 sᴇᴀʀᴄʜ",
                callback_data="mplus HELP_Search",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 4 =================

        [
            InlineKeyboardButton(
                "🍭 🔤 ғᴏɴᴛ",
                callback_data="mplus HELP_Font",
                style=ButtonStyle.DANGER,
            ),

            InlineKeyboardButton(
                "🍭 🤖 ʙᴏᴛs",
                callback_data="mplus HELP_Bots",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 📊 ᴛ-ɢʀᴀᴘʜ",
                callback_data="mplus HELP_TG",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= ROW 5 =================

        [
            InlineKeyboardButton(
                "🍭 📂 sᴏᴜʀᴄᴇ",
                callback_data="mplus HELP_Source",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 ⚖️ ᴛʀᴜᴛʜ-ᴅᴀʀᴇ",
                callback_data="mplus HELP_TD",
                style=ButtonStyle.SECONDARY,
            ),

            InlineKeyboardButton(
                "🍭 🧩 ǫᴜɪᴢ",
                callback_data="mplus HELP_Quiz",
                style=ButtonStyle.PRIMARY,
            ),
        ],

        # ================= ROW 6 =================

        [
            InlineKeyboardButton(
                "🍭 🗣️ ᴛᴛs",
                callback_data="mplus HELP_TTS",
                style=ButtonStyle.DANGER,
            ),

            InlineKeyboardButton(
                "🍭 📻 ʀᴀᴅɪᴏ",
                callback_data="mplus HELP_Radio",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "🍭 📝 ǫᴜᴏᴛʟʏ",
                callback_data="mplus HELP_Q",
                style=ButtonStyle.DANGER,
            ),
        ],

        # ================= BIG BUTTON =================

        [
            InlineKeyboardButton(
                "🍭 ✨ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʀᴏᴏʜɪ ✨ 🍭",
                callback_data="roohi_owner",
                style=ButtonStyle.SECONDARY,
            ),
        ],

        # ================= NAVIGATION =================

        [
            InlineKeyboardButton(
                "☝️ ⏪",
                callback_data="settings_back_helper",
                style=ButtonStyle.SECONDARY,
            ),

            InlineKeyboardButton(
                "🍭 🏠 ʜᴏᴍᴇ 🍭",
                callback_data="mbot_cb",
                style=ButtonStyle.PRIMARY,
            ),

            InlineKeyboardButton(
                "⏩ ☝️",
                callback_data="managebot123 settings_back_helper",
                style=ButtonStyle.SECONDARY,
            ),
        ],

        # ================= CLOSE =================

        [
            InlineKeyboardButton(
                "❌ 🗑 ᴄʟᴏsᴇ 🗑 ❌",
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]