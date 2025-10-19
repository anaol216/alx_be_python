# book_class.py

class Book:
    """
    A class to represent a book with a title, author, and publication year.
    It includes magic methods for initialization, deletion, and string representation.
    """

    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book created: '{self.title}'") # Optional print for demonstration

    def __str__(self):
        """
        String Representation: Provides a user-friendly string for the book (e.g., used by print()).
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Provides an unambiguous string that could recreate the object.
        Format: "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Called when the object is about to be garbage collected.
        Prints a message indicating the book being deleted.
        """
        # Note: The __del__ method is not guaranteed to be called immediately
        # or at all in some Python environments or upon program exit.
        # It is triggered when the object's reference count drops to zero.
        print(f"Deleting '{self.title}'")

# End of book_class.py