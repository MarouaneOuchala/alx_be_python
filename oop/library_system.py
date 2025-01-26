# library_system.py

# Base Class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

# Composition: Library
class Library:
    def __init__(self):
        self.books = []  # A list to store instances of Book, EBook, and PrintBook

    def add_book(self, book):
        if isinstance(book, Book):  # Ensure the added object is an instance of Book or its subclasses
            self.books.append(book)
        else:
            raise ValueError("Only Book instances can be added to the library.")

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook - Title: {book.title}, Author: {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book - Title: {book.title}, Author: {book.author}")
