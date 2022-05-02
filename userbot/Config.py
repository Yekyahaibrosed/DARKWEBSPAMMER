import os

from telethon.tl.types import ChatBannedRights

if ENV := bool(os.environ.get("ENV", False)):
    import os

    class Config(((object))):
        LOGGER = True
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,")
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
 
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "REBELBOT")
        TG_BOT_TOKEN_BF_HER = os.environ.get(
            "TG_BOT_TOKEN_BF_HER", "5098487438:AAEFQ9PbIkXJE1fCOykHhHL90-weMYHUY-o"
        )
        TG_BOT_USER_NAME_BF_HER = os.environ.get(
            "TG_BOT_USER_NAME_BF_HER", "SPAMBOTY8Y7U_BOT"
        )
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        MAX_MESSAGE_SIZE_LIMIT = 4095
    
   
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        if REBELBOT_ID := os.environ.get("REBELBOT_ID", "-1001537981920"):
            REBELBOT_ID = int(REBELBOT_ID)
        if TAG_LOGGER := os.environ.get("TAG_LOGGER", None):
            TAG_LOGGER = int(TAG_LOGGER)
        DB_URI = os.environ.get("DATABASE_URL", None)
        UB_BLACK_LIST_CHAT = {
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        }

  
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
        )

        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", ".")
        HNDLR = os.environ.get("COMMAND_HAND_LER", ".")
        SUDO_USERS = {
            int(x) for x in os.environ.get("SUDO_USERS", "1602757268 5273112771 5279200868").split()
        }

        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", None)
        PLUGIN_CHANNEL = int(os.environ.get("REBELBOT_ID", None))
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/mnmnyp8pa1234/DARK-SPAMDEPLOY"
        )
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        STRING_SESSION1 = os.environ.get("STRING_SESSION1", None)
        STRING_SESSION2 = os.environ.get("STRING_SESSION2", None)
        STRING_SESSION3 = os.environ.get("STRING_SESSION3", None)
        STRING_SESSION4 = os.environ.get("STRING_SESSION4", None)
        BOT_MODE = os.environ.get("BOT_MODE", "ON")
        BOT_TRIGGER = os.environ.get("BOT_TRIGGER", "^/")
        BOTMODE_LOG = int(os.environ.get("BOTMODE_LOG", False))
        FORCE_SUB = os.environ.get("FORCE_SUB", None)
        FORCE_CHANNEL_UN = os.environ.get("FORCE_CHANNEL_UN", None)
        FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
        EXTRA_REBELBOT = os.environ.get("EXTRA_REBELBOT", -1001221881562)
 

else:

    class Config(object):
        DB_URI = None
