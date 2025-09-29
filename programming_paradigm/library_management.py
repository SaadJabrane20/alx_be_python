class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Book '{book.title}' by {book.author} added to the library.")
        else:
            print("Error: Only Book instances can be added.")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"'{book.title}' has been checked out")
                else:
                    print(f"'{book.title}' is already checked out")
                return
        print(f"NO book found with title {title}")

    def return_book(self,title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checket out.")
                return
        print(f"No book found with the title '{title}'. ")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"- {book.title} by {book.author}")
    