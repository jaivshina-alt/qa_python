import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

# Пример теста
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

# Мой тест 1
    def test_add_new_book_book_with_long_name_not_added(self, collector):
        collector.add_new_book('Гарри Поттер, философский камень и принц полукровка')
        assert 'Гарри Поттер, философский камень и принц полукровка' not in collector.get_books_genre()

# Мой тест 2
    def test_add_new_book_duplicates_not_added(self, collector):
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        assert list(collector.get_books_genre().keys()).count('Гарри Поттер и Узник Азкабана') == 1

# Мой тест 3
    def test_set_book_genre_valid_genre_is_set(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert  collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

#Мой тест 4
    def test_set_book_genre_invalid_genre_is_not_set(self, collector):
        collector.add_new_book('Маша и медведь')
        collector.set_book_genre('Маша и медведь', 'Сказка')
        assert  collector.get_book_genre('Маша и медведь') == ''       

# Мой тест 5
    def test_get_books_with_specific_genre_relevant_genres_returned(self, collector): 
        collector.add_new_book('Королевство гнева и тумана') 
        collector.add_new_book('Королевство шипов и роз') 
        collector.add_new_book('Шерлок Холмс') 

        collector.set_book_genre('Королевство гнева и тумана', 'Фантастика') 
        collector.set_book_genre('Королевство шипов и роз', 'Фантастика') 
        collector.set_book_genre('Шерлок Холмс', 'Детективы') 

        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Королевство гнева и тумана', 
            'Королевство шипов и роз'
            ]


# Мой тест 6
    def test_get_books_genre_dict_books_genre_returned(self, collector):
        collector.add_new_book('Королевство крыльев и руин')
        collector.add_new_book('Четвертое крыло')
        assert collector.get_books_genre() == {
            'Королевство крыльев и руин': '',
            'Четвертое крыло': ''
        }

# Мой тест 7
    @pytest.mark.parametrize('age_rated_genres', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_age_rated_genres_excluded(self, collector, age_rated_genres):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', age_rated_genres)
        assert 'Оно' not in collector.get_books_for_children()


# Мой тест 8
    def test_add_book_in_favorites_book_added(self, collector):
        collector.add_new_book('Ониксовый шторм')
        collector.add_book_in_favorites('Ониксовый шторм')
        assert collector.get_list_of_favorites_books() == ['Ониксовый шторм']

# Мой тест 9
    def test_delete_book_from_favorites_book_deleted(self, collector):
        collector.add_new_book('Бедная Лиза')
        collector.add_book_in_favorites('Бедная Лиза')
        collector.delete_book_from_favorites('Бедная Лиза')
        assert collector.get_list_of_favorites_books() == []

# Мой тест 10
    def test_add_book_in_favorites_if_book_doesnt_exist_in_books_genre_it_is_not_added_(self, collector):
        collector.add_book_in_favorites('Книга, которой нет в books_genre')
        assert collector.get_list_of_favorites_books() == []

# Мой тест 11
    def test_add_book_in_favorites_duplicates_not_added(self, collector):
        collector.add_new_book('Гарри Поттер и принц полукровка')
        collector.add_book_in_favorites('Гарри Поттер и принц полукровка')
        collector.add_book_in_favorites('Гарри Поттер и принц полукровка')
        assert collector.get_list_of_favorites_books().count('Гарри Поттер и принц полукровка') == 1