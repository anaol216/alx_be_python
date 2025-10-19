# book_class.py (CORRECTED)

class Book:
    """
    A class to represent a book with a title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.
        NOTE: Removed the print statement to match the expected output.
        """
        self.title = title
        self.author = author
        self.year = year
        # REMOVED: print(f"Book created: '{self.title}'") 

    def __str__(self):
        """
        String Representation: (title) by (author), published in (year)
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Book('title', 'author', year)
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Prints "Deleting (title of the book)" upon object deletion.
        NOTE: Removed the single quotes around {self.title} to match expected output.
        """
        print(f"Deleting {self.title}") # Changed from: print(f"Deleting '{self.title}'")