import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2026705881:AAFRdMqej_hg-zWtH21y-_zXYFFp89fHXXg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7389210"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1040ec4f103f3cb49c8eb13d73a77fdd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001513427093"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1877995595"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001567611014"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", " 𝕨𝕖𝕝𝕔𝕠𝕞𝕖 ❤️\n\n\nGC UTAMA : https://t.me/joinchat/iwIjFSkE4SMwYmY1\n\n\nDONASI PA/VIDEO: @dnspapratevlplus_bot")
try:
    ADMINS=[1248554663]
    for x in (os.environ.get("ADMINS", "1877995595").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
