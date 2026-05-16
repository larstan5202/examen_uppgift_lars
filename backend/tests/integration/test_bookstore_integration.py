import pytest
from src.bookstore import BookStore


@pytest.mark.integration
def test_add_and_toggle_flow():
    store = BookStore()

    b1 = store.addBook("Tolkien", "Sagan om ringen")
    b2 = store.addBook("Adams", "Liftarens guide")

    store.toggleFavorite(b1.id)

    assert b1.is_favorite is True
    assert b1 in store.favorites.favorites
    assert b2.is_favorite is False


@pytest.mark.integration
def test_toggle_favorite_adds_and_remove_from_favorites():
    store = BookStore()
    book = store.addBook("Tolkien", "Sagan om ringen")

    store.toggleFavorite(book.id)
    assert book in store.favorites.favorites

    store.toggleFavorite(book.id)
    assert book not in store.favorites.favorites




