import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from Heroku import cloner, ASSUSERNAME, BOT_NAME
from Heroku.config import API_ID, API_HASH
IMG = ["https://telegra.ph/file/cefd3211a5acdcd332415.jpg", "https://telegra.ph/file/30d743cea510c563af6e3.jpg", "https://telegra.ph/file/f7ae22a1491f530c05279.jpg", "https://telegra.ph/file/2f1c9c98452ae9a958f7d.jpg"]
MESSAGE = "Hᴇʏ! I'ᴍ A Mᴜsɪᴄ Bᴏᴛ Hᴏsᴛᴇʀ/Cʟᴏɴᴇʀ\n\nI Cᴀɴ Hᴏsᴛ Yᴏᴜʀ Bᴏᴛ Oɴ Mʏ Sᴇʀᴠᴇʀ Wɪᴛʜɪɴ Sᴇᴄᴏɴᴅs\n\nTry /clone Tᴏᴋᴇɴ Fʀᴏᴍ @botfather"

@cloner.on_message(filters.private & filters.command("start"))
async def hello(client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/Dhiman_Network"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/Punjabi_Hindi_Chat"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

##Copy from here 

# © By Legend-Dhiman Your motherfucker if uh Don't gives credits.
@cloner.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "Heroku.modules"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @{ASSUSERNAME} To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

