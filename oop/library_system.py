# library_system.py

class Book:
    """
    Base Class: Represents a generic book.
    """
    def __init__(self, title, author):
        """Initializes the title and author."""
        self.title = title
        self.author = author

    def get_details(self):
        """Returns the basic details of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived Class: Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """Initializes EBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size # Unique attribute

    def get_details(self):
        """Overrides the base method to include file size."""
        # Call the base class method to get common details
        base_details = super().get_details().replace("Book: ", "EBook: ")
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived Class: Represents a physical print book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """Initializes PrintBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count # Unique attribute

    def get_details(self):
        """Overrides the base method to include page count."""
        # Call the base class method to get common details
        base_details = super().get_details().replace("Book: ", "PrintBook: ")
        return f"{base_details}, Page Count: {self.page_count}"

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
        """Prints the details of each book in the library using the book's specific get_details method (Polymorphism)."""
        for book in self.books:
            print(book.get_details())

# End of library_system.py