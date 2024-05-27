import os
from enum import Enum
from pathlib import Path

ROOT_ABS_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
ROOT_URL = 'https://app.petflip.xyz/'


class ContentId(Enum):
    IMG_HOME = 'imgs/scr_home2.png'
    IMG_GAME = 'imgs/scr_game2.png'
    IMG_FLIPPED = 'imgs/scr_flipped2.png'
    IMG_CAT_WIN = 'imgs/cat_win2.gif'
    IMG_CAT_LOST = 'imgs/cat_lost2.gif'
    IMG_DOG_WIN = 'imgs/dog_win2.gif'
    IMG_DOG_LOST = 'imgs/dog_lost2.gif'
    HTML_GAME_STATS = 'imgs/game_stats.html'


class StaticContent:

    def __init__(self):
        self._content_bytes = {}

        for e in ContentId:
            with open(self.get_fp(e), 'rb') as f:
                self._content_bytes[e] = f.read()

    @property
    def data(self):
        return self._content_bytes

    def get_bytes(self, cid: ContentId):
        return self._content_bytes[cid]

    @staticmethod
    def get_fp(cid: ContentId):
        return f'{ROOT_ABS_PATH}/{cid.value}'

    @staticmethod
    def get_url(cid: ContentId):
        return f'{ROOT_URL}{cid.value}'

    @staticmethod
    def get_uri(cid: ContentId):
        return f'/{cid.value}'
