"""CoinFlip by @Cattivah
Syntax: .coinflip [optional_choice]"""
import random, re
import asyncio
import time

from asyncio import wait, sleep
from telethon import events
from userbot.system import register, dev_cmd


@bot.on(dev_cmd(pattern="coin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "testa":
            await event.edit("È uscito: **Testa**. \n Hai indovinato.")
        elif input_str == "croce":
            await event.edit("È uscito: **Testa**. \n Mi dispiace, hai perso.")
        else:
            await event.edit("È uscito: **Testa**.")
    elif r % 2 == 0:
        if input_str == "croce":
            await event.edit("È uscito: **Croce**. \n Hai indovinato.")
        elif input_str == "testa":
            await event.edit("È uscito: **Croce**. \n Mi dispiace, hai perso.")
        else:
            await event.edit("È uscito: **Croce**.")
    else:
        await event.edit("¯\_(ツ)_/¯")