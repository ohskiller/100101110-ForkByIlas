# For TeleBot
# By @AKASH_AM1 and @xditya
# Kangers keep credits 
from userbot import ALIVE_NAME
from userbot.system import dev_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Ilas"

#@command(outgoing=True, pattern="^.ded$")
@bot.on(dev_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.edit(" ==             |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
K = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - -\n"
"_/﹋\_\n")
G = ("........___________________\n"
"....../ `-___________--_____|] - - - - - -\n"" - - ░ ▒▓▓█D \n"
"...../==o;;;;;;;;______.:/\n"
".....), -.(_(__) /\n"
"....// (..) ), —\n"
"...//___//\n")
D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
H = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, my friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

@bot.on(dev_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await monster.edit(M)
@bot.on(dev_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    await pig.edit(P)
@bot.on(dev_cmd(pattern=r"kiler"))
async def bluedevikiller(kiler):
    await kiler.edit(K)
@bot.on(dev_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    await gun.edit(G)
@bot.on(dev_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    await dog.edit(D)
@bot.on(dev_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf):
    await hmf.edit(H)
