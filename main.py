from datetime import datetime


class Notes:
    def __int__(self, ID, title, body):
        self.id = ID
        self.title = title
        self.body = body
        self.time = datetime.now()
