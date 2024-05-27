import os
from enum import Enum
from pathlib import Path


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

    def __init__(
        self,
        root_fp,
        root_url,
        load_data=True
    ):
        self._root_fp = root_fp
        self._root_url = root_url

        self._content_bytes = {}

        if load_data:
            for e in ContentId:
                with open(self.get_fp(e), 'rb') as f:
                    self._content_bytes[e] = f.read()

    @property
    def data(self):
        return self._content_bytes

    def get_fp(self, cid: ContentId):
        return f'{self._root_fp}/{cid.value}'

    def get_url(self, cid: ContentId):
        return f'{self._root_url}{cid.value}'

    def get_bytes(self, cid: ContentId):
        return self._content_bytes[cid]

    @staticmethod
    def get_uri(cid: ContentId):
        return f'/{cid.value}'
