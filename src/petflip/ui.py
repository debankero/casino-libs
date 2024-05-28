from telegram import InlineKeyboardButton


class ScrSetup:
    def __init__(
        self, id_: str,
        img: str,
        msg: str,
        kb,
        is_anim: bool = False,
        render_mode: str = 'HTML',
        text_delay: float = 0
    ):
        self.id = id_
        self.img = img
        self.msg = msg
        self.kb: list[list[InlineKeyboardButton]] = kb
        self.is_anim = is_anim
        self.render_mode = render_mode
        self.text_delay = text_delay

    def to_json(self):
        kb = None
        if self.kb:
            kb = []
            for row in self.kb:
                new_row = []
                kb.append(new_row)
                for button in row:
                    new_row.append([button.text, button.callback_data])

        return {
            'id': self.id,
            'img': self.img,
            'msg': self.msg,
            'kb': kb,
            'is_anim': self.is_anim,
            'render_mode': self.render_mode,
            'text_delay': self.text_delay
        }

    @staticmethod
    def from_json(o):
        kb = o['kb']
        new_kb = None
        if kb:
            new_kb = []
            for row in kb:
                new_row = []
                new_kb.append(new_row)
                for button in row:
                    new_row.append(InlineKeyboardButton(button[0], callback_data=button[1]))

        return ScrSetup(
            o['id'], o['img'], o['msg'], new_kb, o['is_anim'], o['render_mode'], o['text_delay']
        )
