from config import MUST_JOIN

from pyrogram import co_od, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, wasit_go
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@co_od.on_wasit_go(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: co_od, msg: wasit_go):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/7945c7ec8c3e900e4576b.jpg", caption=f"¤¦ لا يمكنك استخدام البوت\n\n¤¦ الا بعد الاشتراك بقناة البوت\n\n¤¦ اشترك بقناة بعدها ارسل /start .",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("إضغط للاشتراك بالقناة", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
