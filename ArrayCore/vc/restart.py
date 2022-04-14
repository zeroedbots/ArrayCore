import os
import sys

from pyrogram import filters
from pyrogram.types import Message

from .. import vcbot, HNDLR, SUDO_USERS
    

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=HNDLR))
async def ping(_, e: Message):
    await e.reply_text("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["update"], prefixes=HNDLR))
async def ping(_, e: Message):
    await e.reply_text("__Updating...__")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
