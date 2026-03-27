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

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        return collector
    
    
    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_add_new_genre(self, collector, genre):
        book_name='Гордость и предубеждение и зомби'
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name)== genre

    
    def test_get_book_genre_show_name_book(self, collector):
        book_name='Гордость и предубеждение и зомби'
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.books_genre.get(book_name) == 'Ужасы'

    
    def test_get_books_with_specific_genre_list_genre_book(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_new_book('Доктор Айболит')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Идиот', 'Фантастика')
        collector.set_book_genre('Доктор Айболит', 'Ужасы')
        collector.set_book_genre('Преступление и наказание', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика')==['Идиот', 'Преступление и наказание']
    
    
    def test_get_books_genre_list_of_genre(self):
        genre_collector = BooksCollector()
        genre_collector.add_new_book('Новая книга')
        genre_collector.set_book_genre('Новая книга', 'Комедии')
        assert genre_collector.books_genre == {'Новая книга': 'Комедии'}

    
    def test_get_books_for_children_show_books(self):
        collector = BooksCollector()
        collector.add_new_book('Доктор Айболит')
        collector.set_book_genre('Доктор Айболит', 'Мультфильмы')
        assert 'Доктор Айболит' in collector.get_books_for_children()

     
    def test_add_book_in_favorites_book_is_added(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()
    
    
    def test_delete_book_from_favorites_book_is_deleted(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert ('Гордость и предубеждение и зомби') not in collector.get_list_of_favorites_books()
    
    
    def test_get_list_of_favorites_books_show_list_favorites(self, collector):
        book_name='Гордость и предубеждение и зомби'
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]
