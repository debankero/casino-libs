class UpdateMessage:
    def __init__(self, telegram_id: int, user_context: dict):
        self.telegram_id = telegram_id
        self.user_context = user_context
