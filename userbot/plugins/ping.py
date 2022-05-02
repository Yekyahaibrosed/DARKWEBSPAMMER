from datetime import datetime

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "__**(❛ ᑭσɳց ❜!__**")
    await event.edit(
        f"__**sᴇxʏ sᴘᴀᴍᴍᴇʀ ɪꜱ ᴏɴʟɪɴᴇ..__**\n\n   ⚘ {(datetime.now() - datetime.now()).microseconds / 1000}\n   ⚘ __**ᴏᴡɴᴇʀ**__ ༆ᴅᴀʀᴋ ✰ ᴡᴇʙ༆"
    )