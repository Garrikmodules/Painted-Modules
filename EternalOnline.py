from pyrogram import Client, filters
import time
from pyrogram.raw import functions
import asyncio
import requests
import sys
import os
def datadef():
    return {"name":"EternalOnline","help":"%online %offline","description":"Eternal online"}
@Client.on_message(filters.command("online", prefixes="%") & filters.me)
async def online(client, message):
	await message.edit_text("**Eternal Online On!**")
	await client.send(functions.account.UpdateStatus(offline=False))
@Client.on_message(filters.command("offline", prefixes="%") & filters.me)
async def offline(client, message):
	await message.edit_text("**Eternal Online Off**")
	os.execl(sys.executable, sys.executable, *sys.argv)