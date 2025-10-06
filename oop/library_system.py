class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"Ebook: {self.title} by {self.author} {self.file_size}"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"Print book: {self.title} by {self.author} {self.page_count}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        if isinstance(book, Book):
            print(f"added: {book}")
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")
    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(f"- {book}")