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

    @pytest.fixture(autouse=True)
    def book():
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        return book
    
    @pytest.mark.parametrize('book',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_add_new_genre(self, book, genre):
        book.set_book_genre(book, genre)
        assert self.get_book_genre[book]== self.genre

    @pytest.fixture(autouse=True)
    def test_get_book_genre_show_name_book(self, book):
        book.set_book_genre(book, 'Ужасы')
        assert self.get_book_genre(book) == 'Ужасы'

    def test_get_books_with_specific_genre_list_genre_book(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_new_book('Доктор Айболит')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Идиот', 'Фантастика')
        collector.set_book_genre('Доктор Айболит', 'Ужасы')
        collector.set_book_genre('Преступление и наказание', 'Фантастика')
        assert self.books_with_specific_genre('Фантастика')==['Идиот', 'Преступление и наказание']
    
    def test_get_books_genre_list_of_genre(self):
        genre_collector = BooksCollector()
        genre_collector.add_new_book('Новая книга')
        genre_collector.set_book_genre('Комедия')
        assert 'Комедия' in self.books_genre 

    def test_get_books_for_children_show_books(self):
        collector = BooksCollector()
        collector.add_new_book('Доктор Айболит')
        collector.set_book_genre('Мультфильмы')
        assert 'Доктор Айболит' in self.books_for_children

    @pytest.fixture(autouse=True)
    def test_add_book_in_favorites_book_is_added(self, book):
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in self.favorites

    @pytest.fixture(autouse=True)
    def test_delete_book_from_favorites_book_is_deleted(self, book):
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert ('Гордость и предубеждение и зомби') not in self.favorites
    
    @pytest.fixture(autouse=True)
    def test_get_list_of_favorites_books(self):
        


        
