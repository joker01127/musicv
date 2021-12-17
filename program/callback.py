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
        f"""✨ **اهلا عزيــزي {message.from_user.mention()} !**\n
💭**انــا [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

♲ **❖- يمـكننــي ان اقــوم بتشــغيـل الاغــانـي او الفـيديــوهـات داخــل المحــادثــات الصــوتـيــه..♡**

♲ **❖- قــم باضــافة الحســاب المســاعد وابـدا الحــفلـه.. ❀**
""",
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الــيك كيــفيه اسـتخـدام البــوت:**

1.) **اولا قــم باضــافتـي الي مجموعــتك.**
2.) **بعد ذلك ، قم بترقيتي مشــرف ومنحي جميع الصلاحيات باستثناء التخفي.**
3.) **بعد ترقيتي اكتب, /reload لتحديث قائمه الادمنيه.**
3.) **قم باضافت @{ASSISTANT_NAME} الي مجموعتك.**
4.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو او الاغاني .**

📌 **إذا لم ينضم الحساب المساعد إلي المحادثه الصوتيه ، فتأكد من تشغيلها بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مرة أخرى**

💡 **اذا واجهتك مشكله تواصل معنا عن طريق جروب الدعم: @{GROUP_SUPPORT}**

⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجـــوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اتبع الازرار من الاسفل للمتابعه**

⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمن", callback_data="cbadmin"),
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
        f"""🏮 اليك الاوامر الاساسيه:

» تشغيل - لتشغيل الاغنيه 
» فيديو - لتشغيل الفيدوهات
» تحكم - لعرض قائمه التشغيل
» بحث - لتنزيل فيديو
» صوت - لتنزيل اغنيه

» السرعه - عرض حاله البوت
» /uptime - عرض وقت تحديث البوت

⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اليك اوامر الادمنيه:

» توقف - توقف البث
» استمرار - اعاده التشغيل
» تخطي - تخطي الاغنيه الحالي
» توقف - ايقاف الاغنيه
» تحزيث - اعاده تشغيل البوت
» انضم - دعوه الحساب المساعد للجروب
» غادر - مغادره الحساب المساعد المجموعه

⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اليك اوامر المطور :

» مسح - تنظيف جميع الملفات
» الغاء - تنظيف جميع عمليات التحميل
» النظام - عرض معلومات النظام
» تحديث السورس - تحديث البوت الخاص بك الي احدث اصدار
» ريفريش - اعاده تشغيل البوت
» مغادره - طلب مغادره الحساب المساعد لكل المجموعات

⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("انت لست ادمن ف البوت لا يمكنك التحكم به.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **اعدادات** {query.message.chat.title}\n\n⏸ : ايــقاف\n▶️ : تـشغــيل\n⏹ : اغـــلاق",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🗑 اغــلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ لا شيء يتدفق حاليا", show_alert=True)

@Client.on_callback_query(filters.regex("gambol"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"**مطــور الســورس**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "♡المبــرمـج غــامــبول♡", url=f"https://t.me/G8_M_L"
                    ),
                    InlineKeyboardButton(
                        "📣 جــروب الدعــم", url=f"https://t.me/MatrixSupport_Official"
                    ),
                ],
                [
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )
    
    
    @Client.on_callback_query(filters.regex("mat"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"**⊶───≺♪𝐃𝐉 𝐆𝐀𝐌𝐁𝐎𝐋♪≻───⊷**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𖤍 مــطور الســورس", url=f"https://t.me/G8_M_L"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 جــروب الدعــم", url=f"https://t.me/MatrixSupport_Official"
                    ),
                    InlineKeyboardButton(
                        "📣 قنــاه الســورس", url=f"https://t.me/G8_01"
                    ),
                ],
                [
            [[InlineKeyboardButton("🔙 رجــوع", callback_data="cbcmds")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
