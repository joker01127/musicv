# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا عزيزي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر فوق » 📚 زر الاوامر!**

🔖 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق » ❓ طريقه الاستخدام!**""",
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لاستخدام هذا الروبوت:**

1.) **اولا, قم باضافه البوت الي مجموعتك.**
2.) **ثم قم برفع البوت ادمن مع كل الصلاحيات المطلوبه.**
3.) **اكتب /reload لرفع الادمنيه للتحكم ف البوت.**
3.) **قم باضافه @{ASSISTANT_NAME} لمجموعتك لتشغيل الموسيقي عن طريق /userbotjoin.**
4.) **قم بتشغيل المحادثه الصوتيه لتشغيل الموسيقي , الفيديو.**

📌 **اذا واجهت مشكله في انضمام  المساعد اكتب /userbotleave ثم اكتب /userbotjoin لتاكيد دخول المساعد.**

💡 **للمزيد من المعلومات او المساعد تواصل مع المطور من هنا: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا عزيزي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **للتعرف علي اوامر الشتغيل اتبع ازرار الاوامر من الاسفل !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمن", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطورين", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 الاوامر الاساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اليك الاوامر الاساسيه للتشغيل:

» /play - /تشغيل (song name/link) ➥ play music on video chat
» /video - /فيديو (video name/link) ➥ play video on video chat
» /vstream ➥ play live video from yt live/m3u8
» /playlist - /التحكم ➥ show you the playlist
» /vsong (query) ➥ download video from youtube
» /song (query) - download song from youtube
» /lyric (query) ➥ scrap the song lyric
» /search (query) ➥ search a youtube video link

» /ping ➥ show the bot ping status
» /uptime ➥ show the bot uptime status
» /alive ➥ show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اليك اوامر الادمن:

» /pause - /توقف ➥ pause the stream
» /resume ➥ resume the stream
» /skip - /تخطي ➥ switch to next stream
» /stop - /توقف ➥ stop the streaming
» /vmute ➥ mute the userbot on voice chat
» /vunmute ➥ unmute the userbot on voice chat
» /volume `1-200` ➥ adjust the volume of music (userbot must be admin)
» /reload ➥ reload bot and refresh the admin data
» /userbotjoin ➥ invite the userbot to join group
» /userbotleave ➥ order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر المطورين:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الاعدادات** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
