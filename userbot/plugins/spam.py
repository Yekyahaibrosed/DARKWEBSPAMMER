import asyncio

from REBELBOT.Config import Config
from REBELBOT.utils import admin_cmd, sudo_cmd

LOGGER = Config.PLUGIN_CHANNEL
SUDO_WALA = Config.SUDO_USERS


@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await asyncio.wait(
            [e.respond(str(e.text[8:])) for _ in range(int(e.text[6:8]))]
        )
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@bot.on(admin_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(sanskari):
    if not sanskari.text[0].isalpha() and sanskari.text[0] not in ("/", "#", "@", "!"):
        sanskari_msg = sanskari.text
        for _ in range(1, int(sanskari_msg[9:13])):
            await sanskari.respond(str(sanskari.text[13:]))
        await sanskari.delete()
        if LOGGER:
            await sanskari.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@bot.on(admin_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    await e.delete()
    for _ in range(int("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[1])):
        await e.respond(str("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[2]))
        await asyncio.sleep(
            float("".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)[0])
        )


# @register(outgoing=True, pattern="^.mspam (.*)")
@bot.on(admin_cmd(pattern="mspam (.*)"))
@bot.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
@bot2.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
@bot3.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
@bot4.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
@bot1.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    if sender.id != me.id and not SUDO_WALA:
        return await e.reply("`Sorry sudo users cant access this command..`")
    try:
        await e.delete()
    except:
        pass
    try:
        if not await e.get_reply_message() or not e.reply_to_msg_id or not await e.get_reply_message().media:
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        for _ in range(1, int(e.pattern_match.group(1).split(" ", 1)[0])):
            await e.client.send_file(e.chat_id, await e.get_reply_message().media)
    except:
        return await e.reply(
            "**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )
