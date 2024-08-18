import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# Создал дополнительный файл conftest.py, в который добавил фикстуры создания экземпляра класса BooksCollector(),
# фикстуру добавления новой книги и фикстуру добавления книги в избранное

    # Проверяем, что у добавленной книги нет жанра
    def test_add_new_book_added_without_genre(self, collector, added_book):
        assert collector.get_book_genre(added_book) == ''

    # Проверяем, что невозможно добавить книгу с названием более 40 символов
    def test_add_new_book_with_too_long_name(self, collector):
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # Проверяем возможность установить жанр книги
    # используем параметризацию для проверки сразу нескольких книг
    @pytest.mark.parametrize('name', ['Игра Эндера', 'Основание', 'Атлант расправил плечи'])
    def test_set_book_genre_set_genre_for_books(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'

    # Проверяем, что жанр книге не присвоится, если его нет в списке genre
    def test_set_book_genre_invalid_genre(self, collector, added_book):
        collector.set_book_genre(added_book, 'Приключения')
        assert collector.get_book_genre(added_book) == ''

    # Проверяем, что метод get_book_genre возвращает правильный жанр книги
    def test_get_book_genre_getted_correct_genre(self, collector, added_book):
        collector.set_book_genre(added_book, 'Фантастика')
        assert collector.get_book_genre(added_book) == 'Фантастика'

    # Проверяем, что get_books_with_specific_genre выводит список книг с присвоенным жанром "Фантастика"
    def test_get_books_with_specific_genre_getted_genre_fantasy(self, collector, added_book):
        collector.set_book_genre(added_book, 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == [added_book]

    # Проверяем, что метод get_books_genre возвращает словарь с книгами и их жанрами
    def test_get_books_genre_getted_genres(self, collector, added_book):
        collector.set_book_genre(added_book, 'Фантастика')
        books_genre = collector.get_books_genre()
        assert books_genre[added_book] == 'Фантастика'

    # Проверяем, что метод get_books_for_children не возвращает книги с возрастным ограничением
    def test_get_books_for_children_without_rating(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Тёмная Башня')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Тёмная Башня', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Гарри Поттер' in books_for_children
        assert 'Тёмная Башня' not in books_for_children

    # Проверяем добавление книги в избранное
    def test_add_book_in_favorites_added_in_favorites(self, collector, added_book):
        collector.add_book_in_favorites(added_book)
        favorites = collector.get_list_of_favorites_books()
        assert added_book in favorites

    # Проверяем, что нельзя добавить одну и ту же книгу в избранное дважды
    def test_add_book_in_favorites_cannot_add_duplicate_book_in_favorites(self, collector, favorite_book):
        collector.add_book_in_favorites(favorite_book)
        collector.add_book_in_favorites(favorite_book)
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count(favorite_book) == 1

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites_delited_from_favorites(self, collector, favorite_book):
        collector.delete_book_from_favorites(favorite_book)
        favorites = collector.get_list_of_favorites_books()
        assert favorite_book not in favorites

    # Проверяем, что метод get_list_of_favorites_books возвращает пустой список, если избранных книг нет
    def test_get_list_of_favorites_books_empty(self, collector):
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []
