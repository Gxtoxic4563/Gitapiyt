from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle


def help_pannel(_, START=None):

    upl = InlineKeyboardMarkup(
        [

            # ================= ROW 1 =================

            [
                InlineKeyboardButton(
                    "🍭 🎵 ᴘʟᴀʏ",
                    callback_data="help_callback hb1",
                    style=ButtonStyle.PRIMARY
                ),

                InlineKeyboardButton(
                    "🍭 ⚡ ᴘɪɴɢ",
                    callback_data="help_callback hb2",
                    style=ButtonStyle.SECONDARY
                ),
            ],

            # ================= ROW 2 =================

            [
                InlineKeyboardButton(
                    "🍭 🛡 ᴀᴅᴍɪɴ",
                    callback_data="help_callback hb3",
                    style=ButtonStyle.PRIMARY
                ),

                InlineKeyboardButton(
                    "🍭 🚫 ɢʙᴀɴ",
                    callback_data="help_callback hb4",
                    style=ButtonStyle.DESTRUCTIVE
                ),
            ],

            # ================= ROW 3 =================

            [
                InlineKeyboardButton(
                    "🍭 🎧 sᴏɴɢ",
                    callback_data="help_callback hb5",
                    style=ButtonStyle.SECONDARY
                ),

                InlineKeyboardButton(
                    "🍭 🔁 ʟᴏᴏᴘ",
                    callback_data="help_callback hb6",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ================= BIG BUTTON =================

            [
                InlineKeyboardButton(
                    "🍭 🎮 ғᴜɴ ɢᴀᴍᴇs",
                    callback_data="help_callback hb7",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ================= EXTRA ROW =================

            [
                InlineKeyboardButton(
                    "🍭 📢 ʙʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb8",
                    style=ButtonStyle.DESTRUCTIVE
                ),

                InlineKeyboardButton(
                    "🍭 🛠 ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ",
                    callback_data="help_callback hb9",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ================= EXTRA ROW =================

            [
                InlineKeyboardButton(
                    "🍭 🔍 sᴇᴇᴋ",
                    callback_data="help_callback hb10",
                    style=ButtonStyle.SECONDARY
                ),

                InlineKeyboardButton(
                    "🍭 🎼 sʜᴜғғʟᴇ",
                    callback_data="help_callback hb11",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ================= BIG BUTTON =================

            [
                InlineKeyboardButton(
                    "🍭 ✨ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʀᴏᴏʜɪ ✨ 🍭",
                    callback_data="roohi_help",
                    style=ButtonStyle.SECONDARY
                ),
            ],

            # ================= PAGE NAVIGATION =================

            [
                InlineKeyboardButton(
                    "☝️ ⏪ ᴘʀᴇᴠ",
                    callback_data="help_prev",
                    style=ButtonStyle.SECONDARY
                ),

                InlineKeyboardButton(
                    "🍭 🏠 ʜᴏᴍᴇ 🍭",
                    callback_data="mbot_cb",
                    style=ButtonStyle.PRIMARY
                ),

                InlineKeyboardButton(
                    "ɴᴇxᴛ ⏩ ☝️",
                    callback_data="help_next",
                    style=ButtonStyle.SECONDARY
                ),
            ],

            # ================= CLOSE =================

            [
                InlineKeyboardButton(
                    "❌ 🗑 ᴄʟᴏsᴇ 🗑 ❌",
                    callback_data="close",
                    style=ButtonStyle.DESTRUCTIVE
                ),
            ],
        ]
    )

    return upl