import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ilas"
# ============================================

@bot.on(dev_cmd(pattern=f"alive", outgoing=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running. """
    await alive.edit("ᡕᠵ᠊ᡃ່࡚ࠢ࠘ ᠊߯᠆ࠣ࠘ᡁࠣ࠘᠊᠊ࠢ࠘𐡏 **SISTEMA**\n"
                     f"**> Telethon:** {version.__version__}\n"
                     f"**> Python:** {versions.__python_version__}\n"
                     f"**> Firmware:** {versions.__version__}\n"
                     f"**> Licenza:** {versions.__license__}\n"
                     f"**> Copyright:** Ilas the gay\n"
                     f"›")
