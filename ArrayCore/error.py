import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

HNDLR = os.getenv("HNDLR", "!")

vcbot = Client(
    'ArrayCore',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'ArrayCore.vc'},
)

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
