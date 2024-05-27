from typing import Union

from telegram import Message


class UserState:
    def __init__(
        self,
        last_scr_id: str = None,
        last_pressed_button: str = None,
        payout_amount: float = 0,
        last_msg: Union[Message, None] = None
    ):
        self._last_pressed_button: Union[None, str] = last_pressed_button
        self._last_scr: Union[None, str] = last_scr_id
        self._payout_amount: float = payout_amount
        self._last_msg: Union[None, Message] = last_msg

    @property
    def last_scr(self):
        return self._last_scr

    @property
    def last_pressed_button(self):
        return self._last_pressed_button

    @property
    def payout_amount(self):
        return self._payout_amount

    @property
    def last_msg(self):
        return self._last_msg

    def set_last_scr(self, scr_id: str):
        self._last_scr = scr_id

    def set_last_pressed_button(self, button_id: str):
        self._last_pressed_button = button_id

    def set_payout_amount(self, amount: float):
        self._payout_amount = amount

    def set_last_msg(self, msg: Message):
        self._last_msg = msg


class UserContext:
    def __init__(self):
        self._users: dict[int, UserState] = {}

    def set_last_scr(self, telegram_id: int, scr_id: str):
        if telegram_id in self._users.keys():
            self._users[telegram_id].set_last_scr(scr_id)
        else:
            self._users[telegram_id] = UserState(scr_id)

    def set_last_pressed_button(self, telegram_id: int, button_id: str):
        if telegram_id in self._users.keys():
            self._users[telegram_id].set_last_pressed_button(button_id)
        else:
            self._users[telegram_id] = UserState(None, button_id)

    def set_payout_amount(self, telegram_id: int, amount: float):
        if telegram_id in self._users.keys():
            self._users[telegram_id].set_payout_amount(amount)
        else:
            # This should never happen
            self._users[telegram_id] = UserState(payout_amount=amount)

    def set_last_msg(self, telegram_id: int, msg: Message):
        if telegram_id in self._users.keys():
            self._users[telegram_id].set_last_msg(msg)
        else:
            # This should never happen
            self._users[telegram_id] = UserState(last_msg=msg)

    def get_last_scr(self, telegram_id):
        if telegram_id in self._users.keys():
            return self._users[telegram_id].last_scr
        else:
            return None

    def get_last_pressed_button(self, telegram_id):
        if telegram_id in self._users.keys():
            return self._users[telegram_id].last_pressed_button
        else:
            return None

    def get_payout_amount(self, telegram_id):
        if telegram_id in self._users.keys():
            return self._users[telegram_id].payout_amount
        else:
            return None

    def get_last_msg(self, telegram_id):
        if telegram_id in self._users.keys():
            return self._users[telegram_id].last_msg
        else:
            return None
