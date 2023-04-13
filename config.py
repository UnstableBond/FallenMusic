from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/bed8f502db4beb2011886.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/c311e3206da9228a3a98f.mp4")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/cruel_pain")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pain_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/ed356b970b3bdff749cb1.jpg"
