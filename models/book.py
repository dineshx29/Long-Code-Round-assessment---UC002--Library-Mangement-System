class Book:
    def __init__(self, isbn, title, author, genre, quality="good"):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.quality = quality
        self.status = "available"
    def is_available(self):
        return self.status == "available"
    def update_status(self, status):
        self.status = status