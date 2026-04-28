class BookService:
    def __init__(self):
        self.books = {}
    def add_book(self, book):
        self.books[book.isbn] = book
    def get_book(self, isbn):
        return self.books.get(isbn)
    def list_books(self):
        return self.books.values()
    def search_books(self, keyword):
        keyword = keyword.lower()
        result = []
        for b in self.books.values():
            if (keyword in b.title.lower() or keyword in b.author.lower() or keyword == b.isbn):
                result.append(b)
        return result