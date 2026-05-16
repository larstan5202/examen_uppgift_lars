import pytest
from src.bookstore import Book, FavoriteBooks

@pytest.mark.unit
def test_add_book_to_favorites():
    fav = FavoriteBooks()
    book = Book(1, "Tolkien", "Sagan om ringen")

    fav.add(book)

    assert book in fav.favorites

@pytest.mark.unit
def test_remove_book_from_favorites():
    fav = FavoriteBooks()
    book = Book(1, "Tolkien", "Sagan om ringen")

    fav.add(book)
    fav.remove(book)

    assert book not in fav.favorites
