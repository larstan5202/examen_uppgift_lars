import pytest
from src.bookstore import BookStore


@pytest.mark.unit
def test_add_book_returns_correct_book():
    store = BookStore()
    book = store.addBook("Tolkien", "Sagan om ringen")

    assert book.id == 1
    assert book.author == "Tolkien"
    assert book.title == "Sagan om ringen"
    assert book.is_favorite is False
    assert len(store.books) == 1


@pytest.mark.unit
def test_toggle_favorite_calls_add(mocker):
    store = BookStore()
    book = store.addBook("Tolkien", "Sagan om ringen")

    spy = mocker.spy(store.favorites, "add")

    store.toggleFavorite(book.id)

    spy.assert_called_once_with(book)
    assert book.is_favorite is True


@pytest.mark.unit
def test_toggle_favorite_calls_remove(mocker):
    store = BookStore()
    book = store.addBook("Tolkien", "Sagan om ringen")

    store.toggleFavorite(book.id)  # mark favorite

    spy = mocker.spy(store.favorites, "remove")

    store.toggleFavorite(book.id)  # unmark

    spy.assert_called_once_with(book)
    assert book.is_favorite is False
