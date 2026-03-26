import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23255238"))
API_HASH = getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://files.catbox.moe/om20d5.jpg")
BOT_TOKEN = getenv("BOT_TOKEN", "8541490138:AAHkSAU-mgRnNDfEDfhfcNXywx3z2DvEOnk")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aditya0:aditya0@cluster0.9m8897t.mongodb.net/?appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1003858465326))

OWNER_ID = int(getenv("OWNER_ID", 7812646657))

OWNER = int(getenv("OWNER", 7812646657))

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SONGSONG220/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botbykilwakillua")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/bothub13")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQFMsJ0AZkF_6FO_QOXYM4xr2LTqA9bHWXlZ-qlbe1z59MgkyijM6fPoqPcm86R33T9hwOa8zo0-rJjfEw_M16m37hieo7NiFBH4T_QZGGi2WgIHAZtrIiN4gDkJWP4cNLMFn5kayYRyYW3M16W1phOeecUzhAmwRswx8Zf0jhYc0DJnCNVVbuZZ298obPA5GmuaqS5MJSayndomFXJEMcCxXawW4gS0M6S5DlI-HezzayE8Z7HZJajcbzEiKaApaxr-1h5ycwFZi6TR5E0H9r7PiDiPUABgRm0enJ2UF-B1bQ74EKa-wHiL7jwEQJhlUAHDMXbqmuZwht5DaeyTpnfAjljtRgAAAAH33Bx_AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/om20d5.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/om20d5.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/om20d5.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/om20d5.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/om20d5.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/om20d5.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/om20d5.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/om20d5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/om20d5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/om20d5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/om20d5.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
