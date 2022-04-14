import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime

from .. import vcbot, HNDLR, SUDO_USERS
    
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=HNDLR))
async def restart(_, e: Message):
    await m.reply("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()
