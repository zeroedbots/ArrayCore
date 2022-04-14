import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import time
from datetime import datetime

from ArrayCore.error import vcbot, HNDLR, SUDO_USERS
    
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=HNDLR))
async def restart(_, e: Message):
    if message.sender_chat in SUDO_USERS 
        await e.reply("`Restarting...`")
        os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
        quit()
