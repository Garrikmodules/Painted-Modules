from pyrogram import Client, filters
from time import time
from pyrogram.raw import functions
import asyncio
import requests
@Client.on_message(filters.command("pin", prefixes="%") & filters.me)
async def pin(client, message):
	txt = message.text.replace("%pin ", "")
	print(len(txt))
	if txt == "%pin":
		await message.edit_text("**Need text**")
	else:
		await message.edit_text(txt)
		await message.pin()