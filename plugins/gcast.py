# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2022 𝑩𝒚 @𝑨𝒅𝒊𝒕𝒚𝒂𝑯𝒂𝒍𝒅𝒆𝒓

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["/بث", "/اذاعه"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`🥀 جاري البث...`**")
        if not message.reply_to_message:
            await wtf.edit("**قم بالرد على الرساله المراد الاذاعه به...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**جاري البث...** \n\n**✔️ ارسال الى:** `{sent}` **المحادثات** \n**❌ فشل في:** `{failed}` **المحادثات**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**تم البث بنجاح...**\n\n**✔️ ارسال الى:** `{sent}` **المحادثات**\n**❌ فشل في:** `{failed}` **المحادثات**")
