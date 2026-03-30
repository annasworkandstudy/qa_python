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
    def new_object(self):
        new_object = BooksCollector()
        return new_object
    
    
    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_return_genre_in_list(self, new_object, genre):
        book_name='Гордость и предубеждение и зомби'
        new_object.add_new_book(book_name)
        new_object.set_book_genre(book_name, genre)
        assert new_object.books_genre.get(book_name)== genre

    
    def test_get_book_genre_return_genre_book(self, new_object):
        new_object.add_new_book('Гордость и предубеждение и зомби')
        new_object.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        assert new_object.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    
    def test_get_books_with_specific_genre_return_list_book(self, new_object):
        new_object.add_new_book('Идиот')
        new_object.add_new_book('Доктор Айболит')
        new_object.add_new_book('Преступление и наказание')
        new_object.set_book_genre('Идиот', 'Фантастика')
        new_object.set_book_genre('Доктор Айболит', 'Ужасы')
        new_object.set_book_genre('Преступление и наказание', 'Фантастика')
        assert new_object.get_books_with_specific_genre('Фантастика')==['Идиот', 'Преступление и наказание']
    
    
    def test_get_books_genre_list_of_genre(self, new_object):
        new_object.add_new_book('Новая книга')
        new_object.set_book_genre('Новая книга', 'Комедии')
        assert new_object.get_books_genre() == {'Новая книга': 'Комедии'}

    
    def test_get_books_for_children_return_book(self, new_object):
        new_object.add_new_book('Доктор Айболит')
        new_object.set_book_genre('Доктор Айболит', 'Мультфильмы')
        assert 'Доктор Айболит' in new_object.get_books_for_children()

     
    def test_add_book_in_favorites_show_list_favorites(self, new_object):
        new_object.add_new_book('Гордость и предубеждение и зомби')
        new_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in new_object.get_list_of_favorites_books()
    
    
    def test_delete_book_from_favorites_removes_book(self, new_object):
        new_object.add_new_book('Гордость и предубеждение и зомби')
        new_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        new_object.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert ('Гордость и предубеждение и зомби') not in new_object.get_list_of_favorites_books()
    
    
    def test_get_list_of_favorites_books_is_added_in_favourites(self, new_object):
        new_object.add_new_book('Гордость и предубеждение и зомби')
        new_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(new_object.get_list_of_favorites_books()) == 1


    def test_get_books_for_children_include_age_rating(self, new_object):
        new_object.add_new_book('It')
        new_object.set_book_genre('It', 'Ужасы')
        new_object.add_new_book('Shrek')
        new_object.set_book_genre('Shrek', 'Мультфильмы')
        assert 'Shrek' in new_object.get_books_for_children()
        assert 'It' not in new_object.get_books_for_children()
