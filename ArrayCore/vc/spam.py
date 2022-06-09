# Array 


import asyncio
import re

from pyrogram import Client, filters
from pyrogram.types import Message

from .. import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8,
               Session9, Session10, Session11, Session12,
               Session13, Session14, Session15, Session16,
               Session17, Session18, Session19, Session20,
               Session21, Session22, Session23, Session24,
               Session25, vcbot, hl, SUDO_USERS, HNDLR)


ChatS = ["ArrayCore|RiZoeLXSpam|DNHxHELL|Array|Suzune"]
RiZ = ["@TheRiZoeL|@TheVenomXD|RiZoeL|Akash"]

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
async def spam(_, e: Message):
    usage = ""
    if event.is_group:
       Array = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
       if len(Array) == 2:
           Chat_id = e.chat.id
           Msgg = str(Array[1])
           if re.search(RiZ.lower(), Msgg.lower()):
               return await e.reply_text("Sorry !! I can't Spam on @Arraycore's Owner")
           if int(Chat_id) in GRP:
               return await e.reply_text("Sorry !! I Can't Spam here.")
           counter = int(Array[0])
           ids = 0
           try:
              if Session:
                   ids += 1
                   Session.join_chat(Chat_id)
                   for _ in range(count):
                      await Session.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session2:
                   ids += 1
                   Session2.join_chat(Chat_id)
                   for _ in range(count):
                      await Session2.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session3:
                   ids += 1
                   Session3.join_chat(Chat_id)
                   for _ in range(count):
                      await Session3.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session4:
                   ids += 1
                   Session4.join_chat(Chat_id)
                   for _ in range(count):
                      await Session4.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              if Session5:
                   ids += 1
                   Session5.join_chat(Chat_id)
                   for _ in range(count):
                      await Session5.send_message(chat_id, Msgg)
                      await asyncio.sleep(0.3)
              await vcbot.send_message(e.chat.id, f"**Started Spam** \n\n **Group:** `{Chat_id}` \n **IDs:** `{ids}` \n **Spam Message:** `{Msgg}`")

           except Exception as ex:
                  await vcbot.send_message(e.chat.id, f"Error: `{ex}`")
                  print(ex)  
           







