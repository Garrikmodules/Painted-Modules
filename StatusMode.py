from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
import pyrogram
from pyrogram import Client, filters
def datadef():
    return {"name":"StatusMod","help":"%status typing|upload_photo|upload_video|upload_audio|upload_document|find_location|upload_video_note|choose_contact|playing|speaking|cancel","description":"Fake status"}
@Client.on_message(filters.command("status", prefixes = "%")&filters.me)
def stick(client, msg):
 orig_text=msg.text.split("%status ", maxsplit = 1)[1]
 text = orig_text
 chid=msg.chat.id
 client.send_chat_action(chid, text)
 msg.delete()
