import json
import random
import re
import io
import asyncio
from math import ceil
from userbot import ALIVE_NAME, bot, CMD_LIST
from userbot.system import command
from platform import uname
from telethon import events, errors, custom

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@command(pattern="^.aiuto ?(.*)")
async def cmd_list(event):
    help_string = ""
    pl_amount = 0
    for i in CMD_LIST:
        help_string += i
        help_string += " "
        pl_amount += 1
    help_string = help_string[:-1]
    await event.edit("""◈ **Userbot - Aiuto** ◈
__Developed by @Cattivah__
    
**Utilizzo:**
    `/help [plugin_name]`

**Sistema:**
    Telethon: `1.14.3 Remastered by Ilas v2`
    Python: `3.8.3`

**Plugins ({}):**
    → `{}`
""".format(
        pl_amount,
        help_string
    ))
