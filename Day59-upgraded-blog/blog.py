class Blog:
    def __init__(self, title, subtitle, content, author, date, image_url, blog_id):
        self.blog_id = blog_id
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.author = author
        self.date = date
        self.image_url = image_url
