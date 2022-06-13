## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzYBuzbaSFXfKnptyo2aQZcV1Ebj6BQfdtxvl8WRljVgZxqrRMNl-SU5lMIJTKU36KRmQE3QTxPfQuXZ_UUgnu6BBIE04yza7b_qAgbP-MigdX5_h88k3P7Ff8bJf083InqqjYRbIUzRdMDlQFdDArWNtO80feQABbftkguTa400UK-GgvwGhkO9N3E5wQpeEjE1lupSWD8T_9j3Z6K2Xv3wBPbLQ5-9yciAeuBphgisCw8bxMloMFRPk3ltMsKCocuXuxkneJnCYF9bPRiZus817hjcnE2PtySWQNbXusIcwoPpaKvo9GRcyCNaM2y3yfU1S1xuELigJ8kXkHZJ3DansiA=")
BOT_TOKEN = getenv("BOT_TOKEN", "5500613598:AAF2IOYGQFJdKnOBuQ4-8Z9pT8p6XgDE_8Y")
BOT_NAME = getenv("BOT_NAME", "M𝘶𝘴𝘪𝘤 ")
API_ID = int(getenv("API_ID", "16190152"))
API_HASH = getenv("API_HASH", "e5b18148ae02dadf4c5617f848aeff87")
OWNER_NAME = getenv("OWNER_NAME", "rody")
OWNER_USERNAME = getenv("OWNER_USERNAME", "RODDL")
ALIVE_NAME = getenv("ALIVE_NAME", "rody")
BOT_USERNAME = getenv("BOT_USERNAME", "songmcbot")
OWNER_ID = getenv("OWNER_ID", "5197215524")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "P_LLP")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zzzz5r")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zzzz5r")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1100107939").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
