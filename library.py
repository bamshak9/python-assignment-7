"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(**book):
    library.append(book)
    book_title= book["title"]
    print(f"Book {book_title} added successfully")
    return f"Book {book_title} added successfully"
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    
add_book(id=1, title= "genk", author= "jeremiah", available= True)
add_book(id= 2, title="kishi", author= "john", available= True)
#print(add_book(id=1, title= "Genk", author= "Jeremiah", available= True))
#print(add_book(id= 2, title="kishi", author= "John", available= True))
#print(library)

def search_books(search_param):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """
    for book in library:
        if search_param.lower() in book.values():
            print(book)
        else:
            continue


def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
    for book in library:
        book_title= book["title"]
        if book_id.lower() in book.values():
            return f"You borrowed {book_title}"
        else:
            return f"{book_title} not available"
print(library)
search_books("kishi")
print(borrow_book("genk"))