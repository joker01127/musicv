import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "g8_m_l")
ALIVE_NAME = getenv("ALIVE_NAME", "g8_m_l")
BOT_USERNAME = getenv("BOT_USERNAME", "dj4bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "D_J_H4")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MatrixSupport_Official")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "g8_01")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/da0213215ffeba1eb3602.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Gambol8/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/68e64e7a21d21da897971.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/03724c51b72ddd985616c.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/388491ec29207d78454f4.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/e43692b35fc04afcc059c.jpg")
