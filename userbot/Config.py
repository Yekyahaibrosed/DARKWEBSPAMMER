import os

from telethon.tl.types import ChatBannedRights

if ENV := bool(os.environ.get("ENV", False)):
    import os

    class Config(((object))):
        LOGGER = True
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", None)
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
 
  
        TG_BOT_TOKEN_BF_HER = os.environ.get(
            "TG_BOT_TOKEN_BF_HER", "5098487438:AAEFQ9PbIkXJE1fCOykHhHL90-weMYHUY-o"
        )

        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "REBELBOT")
        # Get a Free API Key from OCR.Space
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
        G_BAN_LOGGER_GROUP = int(os.environ.get("REBELBOT_ID", None))
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
        MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
        MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", None)
        # Telegram BOT Token from @

        TG_BOT_USER_NAME_BF_HER = os.environ.get(
            "TG_BOT_USER_NAME_BF_HER", "SPAMBOTY8Y7U_BOT"
        )
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        MAX_MESSAGE_SIZE_LIMIT = 4095
    
   
        SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
        SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
        SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
        # log

        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )

        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        # pm log
        PM_LOG_GRP_ID = os.environ.get("REBELBOT_ID", None)

        # number of rows of buttons to be displayed in .helpme command
        BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
        # open load
        OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
        OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
        # number of colums of buttons to be displayed in .help command
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
        )
        # pm massage
        CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", "PLEASE DO NOT SPAM MY DM, I WILL REPLY YOU AFTER COME BACK ONLINE!")
        # emoji to be displayed  in help .help
        EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "💙")
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", None)
        HNDLR = os.environ.get("COMMAND_HAND_LER", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do


        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )

       # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)

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
