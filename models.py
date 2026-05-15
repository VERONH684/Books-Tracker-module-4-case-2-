from datetime import datetime

class Book:
    def __init__(self, author: str, title: str, rating: int, date: str = None):
        self.author = author
        self.title = title
        self.rating = rating
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date=data["date"]
        )
