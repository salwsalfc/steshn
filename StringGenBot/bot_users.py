from pyrogram.types import wasit_go
from pyrogram import co_od, filters

from config import OWNER_ID
from StringGenBot.db.users import add_served_user, get_served_users


@co_od.on_wasit_go(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: wasit_go):
    await add_served_user(msg.from_user.id)


@co_od.on_wasit_go(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: wasit_go):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)
