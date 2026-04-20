import random
from datetime import datetime

class Reader:
    """
    Класс, представляющий пассажира авиакомпании.

    Атрибуты:
        first_name (str): Имя читателя
        last_name (str): Фамилия читателя
        patronymic (str): Отчество читателя
        books_on_hand(str): Колличество книг на руках
        book_names (list): Массив наименований книг
        days_since_last_visit (int): Количество дней после последнего посещения
    """

    def __init__(self, first_name, last_name, patronymic, books_on_hand, book_names=None, days_since_last_visit=0):
        """
        Конструктор класса Reader.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.books_on_hand = books_on_hand
        self.book_names = book_names if book_names else []
        self.days_since_last_visit = days_since_last_visit

    def has_overdue_books(self):
        """
        Возвращает true или false, если на руках имеются просроченные книги.
        Если количество дней с последнего посещения больше 14, то взять новые книги не получится.
        """
        return self.days_since_last_visit > 14
    def return_all_books(self):
        """
        Обнуляет количество книг на руках.
        """
        self.books_on_hand = 0
        self.book_names = []
        self.days_since_last_visit = 0
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
    def __str__(self):
        """
        Строковое представление читателя.
        """
        return (f"Читатель: {self.get_full_name()}\n"
                f"Книг на руках: {self.books_on_hand}\n"
                f"Книги: {', '.join(self.book_names) if self.book_names else 'нет'}\n"
                f"Дней после последнего посещения: {self.days_since_last_visit}")

   