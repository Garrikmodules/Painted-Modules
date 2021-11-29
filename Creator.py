#-*-coding: utf-8-*-
from pyrogram import filters, Client
from time import sleep
def datadef():
    return {"name":"Creator","help":"%c %g %s","description":"Create groups/supergroups/channels"}
@Client.on_message(filters.command("c", prefixes="%") & filters.me)
async def c(client, message):
    text=message.text.replace("%c ", "")
    if text == "%c":
    	await message.edit_text("Need args")
    else:
    	result=await client.create_channel(text)
    	await message.edit_text(f"Title: {text} \nID: ```{result.id}```")
    	
@Client.on_message(filters.command("g", prefixes="%") & filters.me)
async def g(client, message):
    text=message.text.replace("%g ", "")
    if text == "%g":
    	await message.edit_text("Need args")
    else:
    	result=await client.create_group(text, 609517172)
    	await message.edit_text(f"Title: {text} \nID: ```{result.id}```")

@Client.on_message(filters.command("s", prefixes="%") & filters.me)
async def s(client, message):
    text=message.text.replace("%s ", "")
    if text == "%s":
    	await message.edit_text("Need args")
    else:
    	result=await client.create_supergroup(text)
    	await message.edit_text(f"Title: {text} \nID: ```{result.id}```")