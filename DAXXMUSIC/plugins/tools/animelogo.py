from pyrogram.types import Message
import random
from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
import requests
from DAXXMUSIC import app
from pyrogram.types import *


#######

button = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/anime_music_robot?startgroup=true",
            )
        ]
]

#####


@app.on_message(filters.command("animelogo"))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("✦ ᴜsᴀɢᴇ ➥ /animelogo Nykaa")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/anime-logo?name={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}",
        caption=f"❖ ᴀɴɪᴍᴇ ʟᴏɢᴏ ʙʏ ➥ [๛˹ɑᴍʀɪᴛ яᴀᴊ˼࿐](https://t.me/ANIME_X_SUPPORTS)",
        reply_markup=InlineKeyboardMarkup(button),
    )


#######

__mod_name__ = "ᴀɴɪᴍᴇ-ʟᴏɢᴏ"

__help__ = """

 ❍ /animelogo ➛ ᴄʀᴇᴀᴛᴇ ᴏᴡɴ ᴛᴇxᴛ ᴀɴɪᴍᴇ ʟᴏɢᴏ ᴡɪᴛʜ ɴʏᴋᴀᴀ.
 """
