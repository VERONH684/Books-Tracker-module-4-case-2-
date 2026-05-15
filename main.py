from storage import load_books, add_book, delete_book
from stats import calculate_average_rating, get_author_statistics

def display_menu() -> None:
    print("\n" + "="*40)
    print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("="*40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("-"*40)

def show_all_books() -> None:
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
    print("\nСПИСОК КНИГ:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.title} - {book.author} (оценка: {book.rating}, дата: {book.date})")

def main() -> None:
    while True:
        display_menu()
        choice = input("Выберите действие (1–6): ").strip()

        if choice == '1':
            author = input("Автор: ").strip()
            title = input("Название: ").strip()
            try:
                rating = int(input("Оценка (1–5): "))
                add_book(author, title, rating)
            except ValueError:
                print("Ошибка: оценка должна быть числом!")

        elif choice == '2':
            show_all_books()

        elif choice == '3':
            books = load_books()
            avg = calculate_average_rating(books)
            print(f"\nСредняя оценка всех книг: {avg}")

        elif choice == '4':
            books = load_books()
            stats = get_author_statistics(books)
            print("\nСТАТИСТИКА ПО АВТОРАМ:")
            for author, data in stats.items():
                print(f"{author}: {data['count']} книг, средняя оценка: {data['average_rating']}")

        elif choice == '5':
            title = input("Введите название книги для удаления: ").strip()
            delete_book(title)

        elif choice == '6':
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
