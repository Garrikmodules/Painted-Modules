from pyrogram import Client, filters
import time
from pyrogram.raw import functions
import asyncio
import requests
import sys
def datadef():
    return {"name":"NicknameMod","help":"on, off","description":"модуль на измену ника"}
@Client.on_message(filters.command("on", prefixes="%") & filters.me)
async def on(client, message):
	fn = message.from_user.first_name
	await client.send(functions.account.UpdateProfile(first_name=fn, last_name="ON ✅"))
	await message.delete()
@Client.on_message(filters.command("off", prefixes="%") & filters.me)
async def off(client, message):
	fn = message.from_user.first_name
	await client.send(functions.account.UpdateProfile(first_name=fn, last_name="OFF ❌"))
	await message.delete()
	sys.exit()	
