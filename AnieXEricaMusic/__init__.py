import asyncio

# Event loop fix for Railway/Python 3.10+
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from AnieXEricaMusic.core.bot import AMBOT
from AnieXEricaMusic.core.dir import dirr
from AnieXEricaMusic.core.git import git
from AnieXEricaMusic.core.userbot import Userbot
from AnieXEricaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AMBOT()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
