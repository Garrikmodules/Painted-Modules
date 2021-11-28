import random
from pyrogram import filters, Client

def datadef():
    return {"name":"Try","help":"%try - *action*","description":"Module for success or failure of an action"}

@Client.on_message(filters.command("try", prefixes="%") & filters.me)
async def trying(client, message):
	do = message.text.replace("%try ", "")
	rnd = random.choice(["Удачно", "Удачно", "Неудачно", "Неудачно", "Удачно", "Неудачно", "Удачно", "Неудачно", "Удачно", "Неудачно"])
	await message.edit_text(f"<b>{do}</b>\n\n<code>{rnd}</code>")