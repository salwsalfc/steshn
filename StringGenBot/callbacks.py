import traceback

from wasit_go import co_od, filters
from wasit_go.types import CallbackQuery, InlineKeyboardMarkup

from StringGenBot.generate import generate_session, ask_ques, buttons_ques


@co_od.on_callback_query(filters.regex(pattern=r"^(generate|wasit_go|wasit_go_bot|تليثون _bot|تليثون )$"))
async def _callbacks(bot: co_od, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("wasit_go") or query.startswith("تليثون "):
        try:
            if query == "wasit_go":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "wasit_go_bot":
                await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "تليثون _bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, تليثون =True, is_bot=True)
            elif query == "تليثون ":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, تليثون =True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "ᴡᴛғ ! sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. \n\n**ᴇʀʀᴏʀ** : {} " \
            "\n\n**ᴩʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @wasit_go**, ɪғ ᴛʜɪs ᴍᴇssᴀɢᴇ " \
            "ᴅᴏᴇsɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ sᴇɴsɪᴛɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ " \
            "ʙᴇᴄᴀᴜsᴇ ᴛʜɪs ᴇʀʀᴏʀ ɪs **ɴᴏᴛ ʟᴏɢɢᴇᴅ ʙʏ ᴛʜᴇ ʙᴏᴛ** !"
