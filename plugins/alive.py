import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
مرحبا انا بوت اغاني
كل الي علي ترفعني مشرف بكروبك و بكامل الصلاحيات


★ المطور ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
★ سورس البوت ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({SOURCE_CODE})
★ قناه التحديثات ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({UPDATES_CHANNEL})
★ ابلاغ عن مشكله ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({SUPPORT_GROUP})



تمتع باغاني عالية الجوده
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ اضفني الى موجموعتك ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", "/فحص"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " انضم الى قناه البوت", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["/repo", "السورس", "/السورس", "سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30c291bae8a73cf534d4a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "للتنصيب اضغط هنا", url=f"{SOURCE_CODE}")
                ]
            ]
        ),
    )
@Client.on_message(filters.command(["/الاوامر", "الاوامر"] & filters.group & ~filters.edited) 
async def help(client: Client, message: Message):
    await m.delete()
    HELP = f"""

<b>👋 اهلا {m.from_user.mention}!

𝘰𝘳𝘥𝘦𝘳𝘴 𝘮𝘶𝘴𝘪𝘤 𝘵𝘦𝘭𝘦𝘵𝘩𝘰𝘯

——————×—————

⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `تشغيل  + اسم الاغنية` ]
———————×———————

⧉ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `استئناف` ] 

⧉ | لأعاده تشغيل الاغنية ⇦  [ `ايقاف_الاستئناف` ]

⧉ | لأيقاف الاغنية  ⇦ [ `ايقاف` ] 

———————×———————

⧉ - `السورس`  // لعرض رابط السورس

———————×———————

🛠 | @N_B_10 

⭐ | @N_B_1

    await m.reply(HELP)
