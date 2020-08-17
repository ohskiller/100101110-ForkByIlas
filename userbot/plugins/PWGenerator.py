# by @Cattivah
# Il plugin è protetto da una licenza copyright.
# È vietato diffonderlo e a renderlo proprio.

import asyncio
import random
from telethon import events
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd


@command()
async def _(event):
    ilass = event.raw_text
    if ilass.startswith('.pwgen'):
        ilas = event.raw_text.split()
        if len(ilas) > 1:
            length = int(ilas[1])
            if 21 > length > 0:
            	length = int(ilas[1])
            else:
            	length = random.randint(9,13)
        else:
        	length = random.randint(9,13)
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
        password = ''
        for c in range(length):
            password += random.choice(chars)
        await event.reply("**◈ Password generata:**\n`" + password + "`\n\n__TIP: Usa .pwgen <numero tra 1 e 20> per generare una password lunga quanto specificato da te.__\n\nCreato da @Cattivah")