def calculate_average_rating(books: list) -> float:
    if not books:
        return 0.0
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)

def get_author_statistics(books: list) -> dict:
    stats = {}
    for book in books:
        if book.author in stats:
            stats[book.author]["count"] += 1
            stats[book.author]["total_rating"] += book.rating
        else:
            stats[book.author] = {"count": 1, "total_rating": book.rating}
    
    for author, data in stats.items():
        data["average_rating"] = round(data["total_rating"] / data["count"], 2)
    
    return stats
