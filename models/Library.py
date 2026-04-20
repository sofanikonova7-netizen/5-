from datetime import datetime

class library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        book_names (list): Массив наименований книг
        book_quantities (list): Массив количества данных книг в библиотеке
        book_genres (list): Массив жанров книг
    """

    def __init__(self,book_names, book_quantities, book_genres ):
        """
        Конструктор класса library.
        """
        self.book_names = book_names
        self.book_quantities =book_quantities 
        self.book_genres = book_genres
    def has_book(self, book_name):
        """
        Проверяет, есть ли книга в библиотеке и доступна ли она.
        """
        if book_name in self.book_names:
            idx = self.book_names.index(book_name)
            return self.book_quantities[idx] > 0
        return False
    def borrow_book(self, book_name):
        """
        Уменьшает количество книг в библиотеке на 1.
        Возвращает True если успешно, иначе False.
        """
        if book_name in self.book_names:
            idx = self.book_names.index(book_name)
            if self.book_quantities[idx] > 0:
                self.book_quantities[idx] -= 1
                return True
        return False
    def get_book_genre(self, book_name):
        """Возвращает жанр книги."""
        if book_name in self.book_names:
            idx = self.book_names.index(book_name)
            return self.book_genres[idx]
        return None
    def __str__(self):
        """Строковое представление библиотеки."""
        result = "Библиотека \n"
        for i, name in enumerate(self.book_names):
            result += f"{name} ({self.book_genres[i]}): {self.book_quantities[i]} шт.\n"
        return result


    