
from datetime import datetime
from models.Reader import Reader
from models.Library import library
from models.Subscription import Subscription

def create_sample_library():
    """Создаёт объект тестовой библиотеки."""
    book_names = [
        "Война и мир",
        "Преступление и наказание",
        "Мастер и Маргарита",
        "Анна Каренина",
        "Идиот",
        "Братья Карамазовы"
    ]
    
    book_quantities = [3, 2, 5, 1, 0, 4]  # 0 - книга "Идиот" недоступна
    
    book_genres = [
        "Роман",
        "Роман",
        "Фантастика",
        "Роман",
        "Роман",
        "Роман"
    ]
    
    return library(book_names, book_quantities, book_genres)


def input_reader_data():
    """Вводит данные читателя с консоли."""
    print("\n Ввод данных читателя")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    patronymic = input("Отчество: ")
    
    books_on_hand = int(input("Количество книг на руках: "))
    
    book_names = []
    if books_on_hand > 0:
        print("Введите наименования книг на руках:")
        for i in range(books_on_hand):
            book = input(f"Книга {i+1}: ")
            book_names.append(book)
    
    days_since_last_visit = int(input("Количество дней после последнего посещения: "))
    
    return Reader(
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        books_on_hand=books_on_hand,
        book_names=book_names,
        days_since_last_visit=days_since_last_visit
    )


def main():
    library = create_sample_library()
    print("\nДоступные книги в библиотеке:")
    print(library)
    reader = input_reader_data()
    if reader.has_overdue_books():
        print(f"\n  У него просрочен абонемент")
        print(f"Прошло {reader.days_since_last_visit} дней с последнего посещения (максимум 14).")
        
        if reader.books_on_hand > 0:
            print("\nУ него есть книги на руках. Пожалуйста, сдайте их.")
            return_books = input("Сдать все книги? (да/нет): ").lower()
            if return_books == "да":
                reader.return_all_books()
                print("Книги сданы.")
            else:
                print("Без сдачи книг вы не можете получить новые книги.")
                return
        else:
            print("Вам необходимо обновить абонемент.")
            return
    
    subscription = Subscription()
    
    if reader.book_names:
        print(f"\nЧитатель хочет получить книги: {', '.join(reader.book_names)}")
        
        success = subscription.process_subscription(reader, library)
        
        if success:
            subscription.print_subscription_info()
        else:
            subscription.print_subscription_info(library)
            print("\nМожем предложить:")
            for book_name in reader.book_names:
                genre = library.get_book_genre(book_name)
                if genre:
                    alternative = library.get_book_by_genre(genre)
                    if alternative and alternative != book_name:
                        print(f"  Вместо '{book_name}' - '{alternative}' ({genre})")
    else:
        print("\nЧитатель не запросил книги.")
    
    print(f"\nИзмененные данные")
    print("\nЧитатель после оформления:")
    print(reader)
    
    print("\nБиблиотека после выдачи:")
    print(library)
