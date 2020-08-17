from telethon import events
from datetime import datetime
from userbot.system import command


@command(pattern="^.test")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**Calcolando...**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("**PINGER**\n__Ping: {}ms__".format(ms))   


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("**PINGER**\n__◈ Ping: {}ms__".format(ms))
