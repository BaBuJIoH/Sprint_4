import pytest

from main import BooksCollector

@pytest.fixture  # Фикстура для создания экземпляра класса BooksCollector
def collector():
    return BooksCollector()

@pytest.fixture  # Фикстура для добавления книги в коллекцию
def added_book(collector):
    book_name = 'Властелин колец'
    collector.add_new_book(book_name)
    return book_name

@pytest.fixture  # Фикстура для добавления книги в избранное
def favorite_book(collector, added_book):
    collector.add_book_in_favorites(added_book)
    return added_book
