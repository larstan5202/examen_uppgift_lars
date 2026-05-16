class Book:
    def __init__(self, book_id, author, title):
        self.id = book_id
        self.author = author
        self.title = title
        self.is_favorite = False


class FavoriteBooks:
    def __init__(self):
        self.favorites = []

    def add(self, book):
        if book not in self.favorites:
            self.favorites.append(book)

    def remove(self, book):
        if book in self.favorites:
            self.favorites.remove(book)


class BookStore:
    def __init__(self):
        self.books = []
        self.favorites = FavoriteBooks()   # ← DENNA RAD ÄR AVGÖRANDE
        self.next_id = 1

    def addBook(self, author, title):
        book = Book(self.next_id, author, title)
        self.books.append(book)
        self.next_id += 1
        return book

    def toggleFavorite(self, book_id):
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            return None

        book.is_favorite = not book.is_favorite

        if book.is_favorite:
            self.favorites.add(book)
        else:
            self.favorites.remove(book)

        return book
