

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
        f""" **مرحــبا {message.from_user.mention()} !**\n
❣️ [{UPDATES_CHANNEL}](https://t.me/{UPDATES_CHANNEL}) **يمكنني تشغيل الموسيقي و الفيديوهات داخل المحادثه الصوتيه**



💫 **للمزيد عن طريقه الاستخدام اتبع الازرار.!**
**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضــف البــوت الـي مجمــوعــتك",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("الاوامـــر 📚", callback_data="cbcmds"),
                ],
                [
                    InlineKeyboardButton(
                        "المـساعــد 👥", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "المــطور ❤️‍🔥", url=f"https://t.me/{OWNER_NAME}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "الــســـورس", url="https://t.me/G8_01"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحــبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اتــبع الازرار من الاســفل لعرض كـافـه الاوامر !**

**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمنيه", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 الاوامر الاساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجــوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر تشغيل البوت ⇓:

» /play + (اسم الاغنيه/الرابط) - للتشغيل الاغنيه ف الكول
» /stream + (الرابط) - لتشغيل البث المباشر صوتي
» /vplay + (اسم الفيديو/link) - لتشغيل الفديو ف الكول
» /vstream - لتشغيل البث المباشر فيديو
» /playlist - عرض قائمه التشغيل
» /video (query) - تنزيل الفيديو من اليوتيوب
» /song (query) - تنزيل الاغنيه من اليوتيوب
» /lyric (query) - لجلب كلمات الاغنيه
» /search (query) - للبحث عن طريق اللينك ف اليوتيوب

» /ping - عرض حالة البوت 
» /uptime - عرض حالة البوت للتشغيل
» /alive - عرض معلومات البوت للتشغيل (في مجموعة)

**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اليك اوامر الادمنيه:

» /pause - ايقاف التشغيل مؤقتا
» /resume - استئناف التشغيل
» /skip - تشغيل الاغنيه التاليه
» /stop - ايقاف تشغيل الموسيقى
» /vmute - كتم البوت في الدردشه الصوتيه
» /vunmute - الغاء كتم البوت في الدردشه الصوتيه
» /volume `1-200` - ضبط مستوي الصوت
» /reload - اعاده تحميل البوت وتحديث الادمنيه
» /userbotjoin - انضمام إلي مجموعتك
» /userbotleave - خروج من المجموعه

**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اليك اوامر المطور:

» /rmw - تنظيف كافة الملفات 
» /rmd - تنظيف كافة الملفات التي تم تنزيلها
» /sysinfo - عرض معلومات النظام
» /update - تحديث بوتك الي اخر اصدار
» /restart -  اعاده تشغيل البوت
» /leaveall - خروج البوت من جميع المجموعات

**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
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
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغــلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ لا يتم البث", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 بطل لعب يعبيط !", show_alert=True)
    await query.message.delete()
