import json
from typing import List
from models import Book

FILENAME = "books.json"

def load_books() -> List[Book]:
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books: List[Book]) -> None:
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=2)

def add_book(author: str, title: str, rating: int) -> bool:
    books = load_books()
    if 1 <= rating <= 5:
        new_book = Book(author, title, rating)
        books.append(new_book)
        save_books(books)
        print("Книга успешно добавлена!")
        return True
    else:
        print("Оценка должна быть от 1 до 5!")
        return False

def delete_book(title: str) -> bool:
    books = load_books()
    original_count = len(books)
    books = [b for b in books if b.title.lower() != title.lower()]
    if len(books) < original_count:
        save_books(books)
        print("Книга удалена!")
        return True
    else:
        print("Книга не найдена!")
        return False
