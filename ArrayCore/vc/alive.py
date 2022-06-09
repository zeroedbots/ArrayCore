from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

Array = ALIVE_PIC or "https://telegra.ph/file/fea7a0ef15a02dd5e4aac.jpg"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if Session:
            ids += 1
        if Session2:
            ids += 1
        if Session3:
            ids += 1
        if Session4:
            ids += 1
        if Session5:
            ids += 1
        if Session6:
            ids += 1
        if Session7:
            ids += 1
        if Session8:
            ids += 1
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Aʀʀᴀʏ ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/DNHxHELL) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/The-HellBot/ArrayCore")
                ]],
        ),
    ) 
    except Exception as lol:         
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Aʀʀᴀʏ ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/DNHxHELL) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• Channel •", url="https://t.me/ArrayCore"),
                ],
                [
                    InlineKeyboardButton("• Repo •", url="https://github.com/The-HellBot/ArrayCore"),
                ],
            ],
        ),
    ) 
