import asyncio

# Patch uvloop's EventLoopPolicy to be safe on Python 3.10+ before any imports
try:
    import uvloop as _uvloop
    _orig_policy_get = _uvloop.EventLoopPolicy.get_event_loop
    def _safe_policy_get(self):
        try:
            return _orig_policy_get(self)
        except RuntimeError:
            loop = self.new_event_loop()
            self.set_event_loop(loop)
            return loop
    _uvloop.EventLoopPolicy.get_event_loop = _safe_policy_get
    _uvloop.install()
except (ImportError, AttributeError):
    pass

# Force create and set a clean event loop
_loop = asyncio.new_event_loop()
asyncio.set_event_loop(_loop)

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
