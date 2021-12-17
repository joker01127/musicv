from datetime import datetime
from sys import version_info
from time import time

from config import (
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
        f"""✨ **اهلا عزيــزي {message.from_user.mention()} !**\n
💭**انــا [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

♲ **❖- يمـكننــي ان اقــوم بتشــغيـل الاغــانـي او الفـيديــوهـات داخــل المحــادثــات الصــوتـيــه..♡**

♲ **❖- قــم باضــافة الحســاب المســاعد وابـدا الحــفلـه.. ❀**
**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✗ اضــف البــوت الـي مجــموعــتك ✗",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],   
                [
                    InlineKeyboardButton("↺ الاوامـــر", callback_data="cbcmds"),
                    InlineKeyboardButton("طــريقـه اسـتخـدام البــوت", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 جــروب الدعــم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قنــاه البــوت", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👤 الحــساب المــساعــد", url="https://t.me/{ASSISTANT_NAME}"
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
                InlineKeyboardButton("✨  جــروب الدعــم", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 قنــاه البــوت", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**مــرحبــا {message.from_user.mention()}, انــا {BOT_NAME}**\n\n✨ اعمــل بشــكل صحــيح\n🍀 مــطـور البــوت: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ وقت التـحديـث: `{uptime}`\n\n**❖ شكرا لاضـافتي هنـا يمـكننــي ان اقــوم بتشــغيـل الاغــانـي او الفـيديــوهـات داخــل المحــادثــات الصــوتـيــه** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["السرعه", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `سرعــه!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["تحديث", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حــالـه البــوت:\n"
        f"• **تحديث:** `{uptime}`\n"
        f"• **وقت التشغيل:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **شـكرا لاضــافتي الي مجــموعــتك !**\n\n"
                "**ارفعنــي مشــرف مـع الصـلاحــيات المطلــوبـه ثـم اكــتـب /userbotjoin لكـي ينـضم الحســاب المـساعــد.**\n\n",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 قنــاه البــوت", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("💭  جــروب الدعــم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("👤 الحــساب المــساعــد", url=f"https://t.me/{ASSISTANT_NAME}")
                        ]
                    ]
                )
            )
