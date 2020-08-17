"""Auto Profile Updation Commands
.autoname for time along name 
.autopic tilted image along with time
.autobio  for time along with your bio
"""
import asyncio
import time
import random, re
import os
import shutil

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot import bot, AUTONAME, DEFAULT_BIO, CMD_HELP
from userbot.system import dev_cmd, command

# ================= CONSTANT =================
DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else "ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ"
DEL_TIME_OUT = 30
DEFAULTUSER = str(AUTONAME) if AUTONAME else "Ilas" 
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
# ============================================


@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    await event.edit(f"Autopic avviato.") 
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n  Time: %H:%M \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((350, 350), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(30)
        except:
            return
        
@bot.on(dev_cmd(pattern="autoname"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"Auto Name avviato.") 
    while True:
        DM = time.strftime("%d/%m/%y")
        HM = time.strftime("%H:%M")
        name = f"Oggi è il {DM} e sono le {HM}"
        logger.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        await asyncio.sleep(DEL_TIME_OUT)
    

@bot.on(dev_cmd("autobio"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"Auto bio avviata.") 
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M")
        bio = f"📅 Oggi è il {DMY} e sono le {HM}"
        logger.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        await asyncio.sleep(DEL_TIME_OUT)
