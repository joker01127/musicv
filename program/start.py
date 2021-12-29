from datetime import datetime
from sys import version_info
from time import time

from config import (
    IMG_5,
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""
╭━❲☆[sᴏᴜʀᴄᴇ ᴅᴊ ɢᴀᴍʙᴏʟ](t.me/G8_01)☆❳━╮
✨ **مرحبا  {message.from_user.mention()} !**
 💭 **انا بوت** [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **يمكنني ان اقوم بالتالي**
💡 - **تشغيل الاغاني و الفيديوهات داخل المحادثه الصوتيه**
 ❓- **للمزيد عن البوت و الاستخدام اتبع الازرار**
╰━❲☆[sᴏᴜʀᴄᴇ ᴅᴊ ɢᴀᴍʙᴏʟ](t.me/G8_01)☆❳━╯
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك ❖",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("📚 الاوامر", callback_data="cbcmds"),
                    InlineKeyboardButton("❓ طريقه الاستخدام", callback_data="cbhowtouse")
                ],
                [
                    InlineKeyboardButton(
                        "مطور السورس💭", url=f"https://t.me/G8_M_L"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url="https://t.me/G8_01"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("مطور السورس 💭", url=f"https://t.me/G8_M_L"),
                InlineKeyboardButton(
                    "📣 قناة السورس", url=f"https://t.me/G8_01"
                ),
            ]
        ]
    )

    alive = f"**مرحبا {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ يعمل البوت بشكل طبيعي\n🍀 المطــور: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ نسخة البوت: `v{__version__}`\n🍀 نسخة بيروجرام: `{pyrover}`\n✨ نسخة بايثون: `{__python_version__}`\n🍀 فيثاغورس والترخيص: `{pytover.__version__}`\n✨ التحديث: `{uptime}`\n\n**شكرا لإضافتي هنا ، لتشغيل الفيديو & الموسيقى في دردشة الفيديو الجماعية الخاصة بك** 💭"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["سورس", f"يا سورس"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("مطور السورس 💭", url=f"https://t.me/G8_M_L"),
                InlineKeyboardButton(
                    "📣 قناة السورس", url=f"https://t.me/G8_01"
                ),
            ]
        ]
    )

    alive = f"""
╭━❲☆[sᴏᴜʀᴄᴇ ᴅᴊ ɢᴀᴍʙᴏʟ](t.me/G8_01)☆❳━╮
✨ **مرحبا  {message.from_user.mention()} !**
 💭 **انا بوت** [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **يمكنني ان اقوم بالتالي**
💡 - **تشغيل الاغاني و الفيديوهات داخل المحادثه الصوتيه**
 ❓- **للمزيد عن البوت و الاستخدام اتبع الازرار**
╰━❲☆[sᴏᴜʀᴄᴇ ᴅᴊ ɢᴀᴍʙᴏʟ](t.me/G8_01)☆❳━╯
""",
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )
    
    
    @Client.on_message(
    command(["غامبول", f"خالد","غنبول"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("غــــامــــبـــول ♡", url=f"https://t.me/G8_M_L"),
                InlineKeyboardButton(
                    "📣 قناة السورس", url=f"https://t.me/G8_01"
                ),
            ]
        ]
    )

    alive = f"『المـــطـور غامــبول للتــواصــل اتبـــع الازرار』",
    await message.reply_photo(
        photo=f"{IMG_5}",
        caption=alive,
        reply_markup=keyboard,
    )
    
    
@Client.on_message(command(["بينج", f"ping@{BOT_USERNAME}", "بينج"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `معلومات البينج!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["تحديث", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حالة البوت:\n"
        f"• **التحديث:** `{uptime}`\n"
        f"• **وقت التشغيل:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **شكرا لإضافتي إلى المجموعة !**\n\n"
                "**قم بترقيتي كمسؤول عن المجموعة ، وإلا فلن أتمكن من العمل بشكل صحيح ، ولا تنسى الكتابة /userbotjoin لدعوة المساعد.**\n\n"
                "**لرفع الادمنيه اكتب** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 قناة السورس", url=f"https://t.me/G8_01"),
                            InlineKeyboardButton("مطور السورس💭", url=f"https://t.me/G8_M_L")
                        ],
                        [
                            InlineKeyboardButton("👤 حساب المساعد", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
