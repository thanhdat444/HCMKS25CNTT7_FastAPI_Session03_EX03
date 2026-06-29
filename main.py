from fastapi import FastAPI

books = [

    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },

    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },

    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },

    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": True
    },

    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": False
    }
]

app = FastAPI()


@app.get("/books/statistics")
def books_statistics():
    available = [book for book in books if book["is_available"] == True]
    borrowed = [book for book in books if book["is_available"] == False]

    return {
        "total_books": len(books),
        "available_books": len(available),
        "borrowed_books": len(borrowed)
    }


@app.get("/books/categories")
def books_categories():
    categories = []

    for book in books:
        if (book["category"] not in categories):
            categories.append(book["category"])

    if (not categories):
        return []
    
    return {
        "categories": categories
    }

@app.get("/books/latest")
def books_latest():
    if (not books):
        return {
            "message": "No books available"
        }
    
    biggest_year = books[0]

    for book in books:
        if (biggest_year["year"] < book["year"]):
            biggest_year = book

    
    
    return biggest_year