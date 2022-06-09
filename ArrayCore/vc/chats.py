from pyrogram import filters
from pyrogram.types import Message

from .. import (Session, Session2, Session3, Session4,
               Session5, Session6, Session7, Session8, HNDLR,
                    SUDO_USERS, vcbot)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message):
    inp = e.text[6:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or invite link to join.")
    if inp.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        if Session:
            await Session.join_chat(inp)
            count += 1
        if Session2:
            await Session2.join_chat(inp)
            count += 1
        if Session3:
            await Session3.join_chat(inp)
            count += 1
        if Session4:
            await Session4.join_chat(inp)
            count += 1
        if Session5:
            await Session5.join_chat(inp)
            count += 1
        if Session6:
            await Session6.join_chat(inp)
            count += 1
        if Session7:
            await Session7.join_chat(inp)
            count += 1
        if Session8:
            await Session8.join_chat(inp)
            count += 1
        await e.reply_text(f"**Joined Successfully ✅** \n\n __IDs__: `{count}` \n __Group__: `{inp}`")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    inp = e.text[7:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or chat id to leave.")
    try:
        if Session:
            await Session.leave_chat(inp)
            count += 1
        if Session2:
            await Session2.leave_chat(inp)
            count += 1
        if Session3:
            await Session3.leave_chat(inp)
            count += 1
        if Session4:
            await Session4.leave_chat(inp)
            count += 1
        if Session5:
            await Session5.leave_chat(inp)
            count += 1
        if Session6:
            await Session6.leave_chat(inp)
            count += 1
        if Session7:
            await Session7.leave_chat(inp)
            count += 1
        if Session8:
            await Session8.leave_chat(inp)
            count += 1
        await e.reply_text(f"**Left Successfully ✅** \n\n __IDs__: `{count}` \n __Group__: `{inp}`")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
