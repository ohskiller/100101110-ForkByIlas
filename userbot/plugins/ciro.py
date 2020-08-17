#
# Tutti i diritti riservati.
# 
# Crediti: @Cattivah
#
"""Commands:
.ciro"""

import asyncio
from telethon import events
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"ciro", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**TG5:** Le scuole chiudono a Napoli...")
    await event.sleep(1)
    await event.edit("**CIRO:** È tempo di giocare a Scuole Chiude a Napoli...")
    await event.sleep(1)
    await event.edit("__Ciao Gamer! Facciamo un gioco: ipotizziamo che stai scaricando Scuole Chiuse a Napoli in questo momento: inizi a giocarci e ci rimani in fissa. Facciamo finta che hai capito al volo come funziona: due team composti da 5 giocatori senza casco che si affrontano per distruggersi a vicenda in una mappa piena di obbiettivi e orologi. Tra le centinaia di campioni disponibili, scegli Ciro, ti piace Ciro; con Ciro è facile rubare agli avversari. non hai bisogno di essere il migliore fin da subito, poiché il gioco stesso ti posiziona davanti a stranieri del tuo stesso livello intellettuale; giocandovi e divertendovi diventerai sempre più bravo. È così che vinci il tuo primo orologio. Insieme ad altri quattro sconosciuti è bello, certo, ma ti accorgi che affrontare gli avversari con un gruppo di amici è molto più divertente. Tu puoi essere il uaglio, qualcun altro l'affammoc e così via. Scarica anche tu Scuole Chiuse a Napoli.__")
