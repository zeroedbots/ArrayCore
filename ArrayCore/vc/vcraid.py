import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue, clear_queue

from .. import (call_py1, call_py2, call_py3, call_py4,
                    call_py5, call_py6, call_py7, call_py8, vcbot, 
                    HNDLR, SUDO_USERS, Session)

from .. import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8)

logging.basicConfig(level=logging.INFO)

aud_list = [
    "./ArrayCore/Audio/AUD1.mp3",
    "./ArrayCore/Audio/AUD2.mp3",
    "./ArrayCore/Audio/AUD3.mp3",
    "./ArrayCore/Audio/AUD4.mp3",
    "./ArrayCore/Audio/AUD5.mp3",
    "./ArrayCore/Audio/AUD6.mp3",
    "./ArrayCore/Audio/AUD7.mp3",
    "./ArrayCore/Audio/AUD8.mp3",
    "./ArrayCore/Audio/AUD9.mp3",
    "./ArrayCore/Audio/AUD10.mp3",
    "./ArrayCore/Audio/AUD11.mp3",
    "./ArrayCore/Audio/AUD12.mp3",
    "./ArrayCore/Audio/AUD13.mp3",
    "./ArrayCore/Audio/AUD14.mp3",
    "./ArrayCore/Audio/AUD15.mp3",
    "./ArrayCore/Audio/AUD16.mp3",
    "./ArrayCore/Audio/AUD17.mp3",
    "./ArrayCore/Audio/AUD18.mp3",
    "./ArrayCore/Audio/AUD19.mp3",
    "./ArrayCore/Audio/AUD20.mp3",
]

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vraid"], prefixes=HNDLR))
async def vraid(_, e: Message):
     await e.reply_text(f"__There Is an Error In Command {HNDLR}vraid !! \n We'll Fix It Soon__ \n\n **© @ArrayCore**")

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["praid"], prefixes=HNDLR))
async def vraid(_, e: Message):
     await e.reply_text(f"__There Is an Error In Command {HNDLR}praid !! \n We'll Fix It Soon__ \n\n **© @ArrayCore**")

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    aud1 = choice(aud_list)
    aud2 = choice(aud_list)
    aud3 = choice(aud_list)
    aud4 = choice(aud_list)
    aud5 = choice(aud_list)
    aud6 = choice(aud_list)
    aud7 = choice(aud_list)
    aud8 = choice(aud_list)
    if inp:
        TheVenomXD = await e.reply_text("**Starting VC raid**")
        link = f"https://itshellboy.tk/{aud1[1:]}"
        dl1 = aud1
        dl2 = aud2
        dl3 = aud3
        dl4 = aud4
        dl5 = aud5
        dl7 = aud6
        dl6 = aud7
        dl8 = aud8
        songname = aud1[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl1, dl2, dl3, dl4, dl5, dl6, dl7, dl8, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py1:
                await Session.join_chat(chat_id)
                await call_py1.join_group_call(chat_id, AudioPiped(dl1), stream_type=StreamType().pulse_stream)
            if call_py2:
                await Session2.join_chat(chat_id)
                await call_py2.join_group_call(chat_id, AudioPiped(dl2), stream_type=StreamType().pulse_stream)
            if call_py3:
                await Session3.join_chat(chat_id)
                await call_py3.join_group_call(chat_id, AudioPiped(dl3), stream_type=StreamType().pulse_stream)
            if call_py4:
                await Session4.join_chat(chat_id)
                await call_py4.join_group_call(chat_id, AudioPiped(dl4), stream_type=StreamType().pulse_stream)
            if call_py5:
                await Session5.join_chat(chat_id)
                await call_py5.join_group_call(chat_id, AudioPiped(dl5), stream_type=StreamType().pulse_stream)
            if call_py6:
                await Session6.join_chat(chat_id)
                await call_py6.join_group_call(chat_id, AudioPiped(dl6), stream_type=StreamType().pulse_stream)
            if call_py7:
                await Session7.join_chat(chat_id)
                await call_py7.join_group_call(chat_id, AudioPiped(dl7), stream_type=StreamType().pulse_stream)
            if call_py8:
                await Session8.join_chat(chat_id)
                await call_py8.join_group_call(chat_id, AudioPiped(dl8), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            if call_py6:
                await call_py6.leave_group_call(chat_id)
            if call_py7:
                await call_py7.leave_group_call(chat_id)
            if call_py8:
                await call_py8.leave_group_call(chat_id)
            clear_queue(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            if call_py6:
                await call_py6.pause_stream(chat_id)
            if call_py7:
                await call_py7.pause_stream(chat_id)
            if call_py8:
                await call_py8.pause_stream(chat_id)
            await e.reply_text(f"**VC Raid Paued In:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], prefixes=HNDLR))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Session.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py1:
                await call_py1.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            if call_py6:
                await call_py6.resume_stream(chat_id)
            if call_py7:
                await call_py7.resume_stream(chat_id)
            if call_py8:
                await call_py8.resume_stream(chat_id)
            await e.reply_text(f"**VC Raid Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No raid is currently paused!**")

