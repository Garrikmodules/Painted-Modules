from pyrogram import Client, filters
import time
from pyrogram.raw import functions
def datadef():
    return {"name":"DelMe","help":"%delme *secret*","description":"Delete all your messages"}
@Client.on_message(filters.command("delme", prefixes="%") & filters.me)
async def delme(client, message):
	text = message.text.replace("%delme ", "")
	if text == "delete":
		chat_id=message.chat.id
		user_id=message.from_user.id
		async for message in client.iter_history(chat_id):
 			if message.from_user.id == user_id:
					await message.delete()
	else:
		await message.edit_text("To confirm the action, write after %delme delete")