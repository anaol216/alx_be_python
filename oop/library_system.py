# library_system.py (REVISED with __str__)

class Book:
    """
    Base Class: Represents a generic book.
    """
    def __init__(self, title, author):
        """Initializes the title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """
        Provides a user-friendly string representation for the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived Class: Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """Initializes EBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size # Unique attribute

    def __str__(self):
        """
        Overrides __str__ to include file size for EBook.
        """
        # Call the base class __str__ and modify the prefix
        base_str = super().__str__().replace("Book: ", "EBook: ")
        return f"{base_str}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived Class: Represents a physical print book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """Initializes PrintBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count # Unique attribute

    def __str__(self):
        """
        Overrides __str__ to include page count for PrintBook.
        """
        # Call the base class __str__ and modify the prefix
        base_str = super().__str__().replace("Book: ", "PrintBook: ")
        return f"{base_str}, Page Count: {self.page_count}"

class Library:
    """
    Composition Class: Represents a library that manages a collection of books.
    """
    def __init__(self):
        """Initializes the library with an empty list of books."""
        self.books = [] # Composition: Library "has a" list of books

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book by using the built-in print() function,
        which implicitly calls the object's __str__ method (Polymorphism).
        """
        for book in self.books:
            print(book) # This implicitly calls book.__str__()