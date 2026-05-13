from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle


def help_pannel(_, START=None):

    upl = InlineKeyboardMarkup(
        [

            # ===== FIRST ROW =====

            [
                InlineKeyboardButton(
                    "🎵 Play",
                    callback_data="help_callback hb1",
                    style=ButtonStyle.PRIMARY
                ),

                InlineKeyboardButton(
                    "⚡ Ping",
                    callback_data="help_callback hb2",
                    style=ButtonStyle.SECONDARY
                ),
            ],

            # ===== SECOND ROW =====

            [
                InlineKeyboardButton(
                    "🛡 Admin",
                    callback_data="help_callback hb3",
                    style=ButtonStyle.PRIMARY
                ),

                InlineKeyboardButton(
                    "🚫 Gban",
                    callback_data="help_callback hb4",
                    style=ButtonStyle.DESTRUCTIVE
                ),
            ],

            # ===== THIRD ROW =====

            [
                InlineKeyboardButton(
                    "🎧 Song",
                    callback_data="help_callback hb5",
                    style=ButtonStyle.SECONDARY
                ),

                InlineKeyboardButton(
                    "🔁 Loop",
                    callback_data="help_callback hb6",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ===== BIG BUTTON =====

            [
                InlineKeyboardButton(
                    "🎮 Fun Games",
                    callback_data="help_callback hb7",
                    style=ButtonStyle.PRIMARY
                ),
            ],

            # ===== PAGE NAVIGATION =====

            [
                InlineKeyboardButton(
                    "◀️ Page 1",
                    callback_data="help_prev",
                    style=ButtonStyle.SECONDARY
                ),

                InlineKeyboardButton(
                    "Page 2 ▶️",
                    callback_data="help_next",
                    style=ButtonStyle.SECONDARY
                ),
            ],

            # ===== CLOSE =====

            [
                InlineKeyboardButton(
                    "❌ Close",
                    callback_data="close",
                    style=ButtonStyle.DESTRUCTIVE
                ),
            ],
        ]
    )

    return upl