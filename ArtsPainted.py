import random
from pyrogram import Client, filters
def datadef():
    return {"name":"Arts","info":"%vjuh \n%priletel \n%cowsay \n%padayu \n%xuytebe \n%lol","description":"Mini arts"}
@Client.on_message(filters.command("vjuh", prefixes="%") & filters.me)
async def vjux(client, message):
        text = message.text.replace("%vjuh ", "")
        if not text:
            await message.edit_text('<b>Нет текста после команды :c</b>')
            return
        else:
            vjuh = ("<code>.∧＿∧\n"
                    "( ･ω･｡)つ━☆・*。\n"
                    "⊂  ノ    ・゜ .\n"
                    "しーＪ   °。  *´¨)\n"
                    "             .· ´¸.·*´¨) ¸.·*¨)\n"
                    "                     (¸.·´ (¸.·'* ☆\n\n"
                    f"Вжух и ты <code>{text}</code>")
            await message.edit(vjuh)
@Client.on_message(filters.command("priletel", prefixes="%") & filters.me)
async def priletel(client, message):
	text = message.text.replace("%priletel", "")
	prilitel = ("▬▬▬.◙.▬▬▬\n"
                        "  ═▂▄▄▓▄▄▂\n"
                        "◢◤ █▀▀████▄▄▄▄◢◤\n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                        "◥█████◤ прилетел сказать что-то важное...\n"
                        "══╩══╩═\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        "╬═╬\n"
                        f"╬═╬☻/ - <b>{text}</b>\n"
                        "╬═╬/▌\n"
                        "╬═╬/ \ ")
	await message.edit_text(prilitel)
@Client.on_message(filters.command("cowsay", prefixes="%") & filters.me)
async def cowsay(client, message):
	text = message.text.replace("%cowsay ", "")
	if not text:
            await message.edit('<b>Нет текста после команды :c</b>')
            return
	else:
            cowsay = ("<code> "
                      f"< {text} >\n"
                      "\n"
                      "     \   ^__^\n"
                      "      \  (oo)\_______\n"
                      "         (__)\       )\/\n"
                      "             ||----w||\n"
                      "             ||     ||</code>")
	await message.edit_text(cowsay)
@Client.on_message(filters.command("padayu", prefixes="%") & filters.me)
async def padayu(client, message):
	text = message.text.replace("%padayu ", "")
	if not text:
    			text = ("ПАДАЮ")
	padayu = ("┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      f"┛┗┛┗┛┃ <b>{text}</b>!\n"
                      "┓┏┓┏┓┃ ＼○／\n"
                      "┛┗┛┗┛┃ /\n"
                      "┓┏┓┏┓┃ノ)\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n"
                      "┓┏┓┏┓┃\n"
                      "┛┗┛┗┛┃\n")
	await message.edit_text(padayu)
@Client.on_message(filters.command("xuytebe", prefixes="%") & filters.me)
async def xuytebe(client, message):
	text = message.text.replace("%xuytebe ", "")
	if not text:
            text = ("ХУЙ ТЕБЕ!")
            huytebe = ("...............▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       "................▐▄▀▀▀▀▀▄▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "................▐▒▒▒▒▒▒▒▌\n"
                       "..................▀▌▒▀▒▐▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebe)
	else:
            huytebe = ("...............▄▄▄▄▄\n"
                       "..............▄▌░░░░▐▄\n"
                       "............▐░░░░░░░▌\n"
                       "....... ▄█▓░░░░░░▓█▄\n"
                       "....▄▀░░▐░░░░░░▌░▒▌\n"
                       ".▐░░░░▐░░░░░░▌░░░▌\n"
                       "▐ ░░░░▐░░░░░░▌░░░▐\n"
                       "▐ ▒░░░ ▐░░░░░░▌░▒▒▐ \n"
                       "▐ ▒░░░░▐░░░░░░▌░▒▐\n"
                       "..▀▄▒▒▒▒▐░░░░░░▌▄▀\n"
                       "........ ▀▀▀ ▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       ".................▐░░░░░░▌\n"
                       "................▐▄▀▀▀▀▀▄▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "...............▐▒▒▒▒▒▒▒▒▌\n"
                       "................▐▒▒▒▒▒▒▒▌\n"
                       "..................▀▌▒▀▒▐▀\n"
                       "\n"
                       f"<b>{text}</b>")
            await message.edit(huytebe)
@Client.on_message(filters.command("lol", prefixes="%") & filters.me)
async def lol(client, message):
	lol = ("    ┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
               "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
               "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
               "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
               "┗━━━┛╰━━━━╯┗━━━┛\n")
	await message.edit(lol)