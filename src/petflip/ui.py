class ScrSetup:
    def __init__(
        self, id_: str, img: str, msg: str, kb, is_anim: bool = False, render_mode: str = 'HTML'
    ):
        self.id = id_
        self.img = img
        self.msg = msg
        self.kb = kb
        self.is_anim = is_anim
        self.render_mode = render_mode

    def to_json(self):
        return {
            'id': self.id,
            'img': self.img,
            'msg': self.msg,
            'kb': self.kb,
            'is_anim': self.is_anim,
            'render_mode': self.render_mode,
        }

    @staticmethod
    def from_json(o):
        return ScrSetup(
            o['id'], o['img'], o['msg'], o['kb'], o['is_anim'], o[''], o['render_mode']
        )
