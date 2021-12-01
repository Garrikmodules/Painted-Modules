from pyrogram import Client, filters
import time
from pyrogram.raw import functions
import asyncio
import requests
def datadef():
    return {"name":"IAmGhoul","help":"%ghoul","description":"Ghoul"}
@Client.on_message(filters.command("ghoul", prefixes="%") & filters.me)
async def ghoul(client, message):
			await message.edit_text("Я гуль")
			chat_id=message.chat.id
			a = 1000    
			while a != 6:
				c = str(a)
				a = a - 7
				b = str(a)
				d = c + " - 7 = " + b
				await client.send_message(chat_id, d)