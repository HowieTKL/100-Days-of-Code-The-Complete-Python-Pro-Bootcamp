from email.base64mime import body_encode

class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = int(id)
        self.title = title
        self.subtitle = subtitle
        self.body = body
