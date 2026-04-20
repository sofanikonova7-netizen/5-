class Subscription:
    """
Класс, представляющий абонемент.
    Атрибуты:
        reader_full_name (str): ФИО читателя
        requested_books (list): Массив наименований книг, которые он хочет взять
    """

    def __init__(self):
        """Конструктор класса Subscription."""
        self.reader_full_name = None
        self.requested_books = []

    def check_book_availability(self, reader, library):
        """
 Принимает наименование книги ЧИТАТЕЛЯ, объект типа БИБЛИОТЕКА,
и возвращает значение true или false если есть/нет совпадения.
        """
        for book_name in reader.book_names:
            if library.has_book(book_name):
                return True
        return False
    def process_subscription(self, reader, library):
        """
        Принимает на вход объект типа ЧИТАТЕЛЬ и объект типа БИБЛИОТЕКА,
        и возвращает значение true или false в зависимости от наличия книги в библиотеке.
        Осуществляет оформление абонемента.
        """
        self.reader_full_name = reader.get_full_name()
        self.requested_books = []

        for book_name in reader.book_names:
            if library.has_book(book_name):
                library.borrow_book(book_name)
                self.requested_books.append(book_name)

        return len(self.requested_books) > 0
    def print_subscription_info(self, library=None):
        """Выводит в консоль информацию об абонементе."""
        if self.requested_books:
            print("\n Информация об абонементе")
            print(f"Читатель: {self.reader_full_name}")
            print(f"Выданные книги: {', '.join(self.requested_books)}")
            print(f"Всего книг: {len(self.requested_books)}")
        else:
            print("\nНевозможно выдать книги: нужных книг нет в наличии.")
            if library:
                print("Мы можем предложить вам другие книги из тех же жанров.")
