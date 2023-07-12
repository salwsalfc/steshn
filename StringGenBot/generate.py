from بايروجرام.types import wasit_go
from تليثون  import Telegramco_od
from بايروجرام import co_od, filters
from asyncio.exceptions import TimeoutError
from تليثون .sessions import StringSession
from بايروجرام.types import InlineKeyboardMarkup, InlineKeyboardButton
from بايروجرام.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from تليثون .errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "☆☆• ذا كنت تريد تنصب ميوزك اختار بايروجرام\n\n• واذا تريد تنصب تليثون فأختار تيرمڪس\n\n• يوجد استخرجات جلسات لي البوتات☆☆"


buttons_ques = [
    [
        InlineKeyboardButton("بايروجرام ⭐", callback_data="بايروجرام"),
        InlineKeyboardButton("تلثيون ⭐", callback_data="تليثون "),
    ],
    [
        InlineKeyboardButton("بايروجرام بوت ⭐", callback_data="بايروجرام_bot"),
        InlineKeyboardButton("تلثيون بوت ⭐", callback_data="تليثون _bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" اضغط لبدا استخراج الكود ⭐ ", callback_data="أبدء ♥")
    ]
]




@co_od.on_wasit_go(filters.private & ~filters.forwarded & filters.command(["أبدء ♥", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def أبدء ♥_session(bot: co_od, msg: wasit_go, تليثون =False, is_bot: bool = False):
    if تليثون :
        ty = "تليثون "
    else:
        ty = "بايروجرام"
    if is_bot:
        ty += " ʙᴏᴛ"
    await msg.reply(f"» ⚡ ¦ بـدء إنـشـاء جـلسـة ☆☆{ty}☆☆ ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "🎮حسنـا قم بأرسال الـ API_ID\n\nاضغط /skipلتخطي", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("☆☆يجب ان يكون الـ API_ID عدد صحيحاً، حاول استخراج الجلسة مره اخرى.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» 🎮حسنـا قم بأرسال الـ API_HASH", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» ✔️الان ارسل رقمك مع رمز دولتك , مثال :+201287585064''"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ☆☆ʙᴏᴛ_ᴛᴏᴋᴇɴ☆☆ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply(" انتظر سـوف نـرسـل كـود لحسابك بالتليجـرام .")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if تليثون  and is_bot:
        co_od = Telegramco_od(StringSession(), api_id, api_hash)
    elif تليثون :
        co_od = Telegramco_od(StringSession(), api_id, api_hash)
    elif is_bot:
        co_od = co_od(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        co_od = co_od(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await co_od.connect()
    try:
        code = None
        if not is_bot:
            if تليثون :
                code = await co_od.send_code_request(phone_number)
            else:
                code = await co_od.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply("» ʏᴏᴜʀ ☆☆ᴀᴩɪ_ɪᴅ☆☆ ᴀɴᴅ ☆☆ᴀᴩɪ_ʜᴀsʜ☆☆ ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply("» ᴛʜᴇ ☆☆ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ☆☆ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "[ارسل الكود زي اللي في الصوره](https://telegra.ph/file/da1af082c6b754959ab47.jpg)» 🔍من فضلك افحص حسابك بالتليجرام وتفقد الكود من حساب اشعارات التليجرام. إذا كان\n  هناك تحقق بخطوتين( المرور ) ، أرسل كلمة المرور هنا بعد ارسال كود الدخول بالتنسيق أدناه.- اذا كانت كلمة المرور او الكود  هي\n 12345 يرجى ارسالها بالشكل التالي 1 2 3 4 5 مع وجود مسـافـات بين الارقام اذا احتجت مساعدة @co_od.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply(" تم انتهاء وقت الجلسه 10 دقائق يرجى اعاده استخراج الجلسه من البدايه .", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if تليثون :
                await co_od.sign_in(phone_number, phone_code, password=None)
            else:
                await co_od.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ☆☆ᴡʀᴏɴɢ.☆☆\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ☆☆ᴇxᴩɪʀᴇᴅ.☆☆\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, " ارسل الباسورد الخاص بحسابك .", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply(" تم انتهاء وقت الجلسه 5 دقائق يرجى اعاده استخراج الجلسه من البدايه ..", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if تليثون :
                    await co_od.sign_in(password=password)
                else:
                    await co_od.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if تليثون :
            await co_od.start(bot_token=phone_number)
        else:
            await co_od.sign_in_bot(phone_number)
    if تليثون :
        string_session = co_od.session.save()
    else:
        string_session = await co_od.export_session_string()
    text = f"☆☆جلسة حسابك  {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ☆☆ \n\n`{string_session}` \n\n☆☆ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :☆☆ @co_od \n♕ ☆☆ɴᴏᴛᴇ :☆☆ حافظ علية ولاتعطية الى اي شخص قد يخترق حسابك او يقوم بحذفة بواسطة هاذه الكود لاتعطية
الى اي شخص بيها\n انضم هناا فضلا @wasit_go 🥺"
    try:
        if not is_bot:
            await co_od.send_wasit_go("me", text)
        else:
            await bot.send_wasit_go(msg.chat.id, text)
    except KeyError:
        pass
    await co_od.disconnect()
    await bot.send_wasit_go(msg.chat.id, "» ✅تم استخراج الجلسه بنجاح ️ {} .\n\n🔍من فضلك اذهب الي الرسايل المحفوظه بحسابك!  ! \n\n☆☆ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ☆☆ @co_od 🥺".format("تليثون " if تليثون  else "بايروجرام"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("☆☆ تم تنفيذ طلبك انتهت عملية ل بداية اكتب /start !☆☆", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("☆☆» تم اعادة تشغيل من بوت تيرمكس  !☆☆", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("☆☆» تم الغاء عملية استخراج الجلسه ☆☆", quote=True)
        return True
    else:
        return False
