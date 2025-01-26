# library_system.py

# Base Class: Book
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        if file_size <= 0:
            raise ValueError("File size must be a positive integer.")
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        if page_count <= 0:
            raise ValueError("Page count must be a positive integer.")
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition: Library
class Library:
    def __init__(self):
        self.books = []  # A list to store instances of Book, EBook, and PrintBook

    def add_book(self, book: Book):
        if isinstance(book, Book):  # Ensure the added object is an instance of Book or its subclasses
            self.books.append(book)
        else:
            raise ValueError("Only Book instances can be added to the library.")

    def list_books(self):
        for book in self.books:
            print(book)
