import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN","5881922540:AAE6ogxr3ENJ1SN3BBkYdTEAPSa-jl_E3TQ")
BOT_NAME = getenv("BOT_NAME", "MUSTAR_X7bot")
API_ID = int(getenv("API_ID","28836784"))
API_HASH = getenv("API_HASH","fb59b0cbdeb3e9e97db1f9fe61b5e8f1")
OWNER_NAME = getenv("OWNER_NAME", "MR_X_N0")
ALIVE_NAME = getenv("ALIVE_NAME", "MR_X_N0")
BOT_USERNAME = getenv("BOT_USERNAME", "MUSTAR_X7bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MR_X_N0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MUSTAR_X7")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MUSTAR_X8")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5838699780").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ".").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/joker01127/musicv")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/3dbef9fb9cbc7ad4318d6.jpg")
