from abc import ABC, abstractmethod

# SRP: Клас Book відповідає лише за зберігання даних про книгу
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# ISP: Інтерфейс визначає чіткий набір методів для роботи з бібліотекою
class LibraryInterface(ABC):
    @abstractmethod
    def add(self, book: Book):
        pass

    @abstractmethod
    def remove(self, title: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

# OCP та LSP: Клас Library реалізує інтерфейс і може бути замінений будь-якою іншою реалізацією LibraryInterface
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add(self, book: Book):
        self.books.append(book)

    def remove(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def get_all(self):
        return self.books

# DIP: LibraryManager залежить від абстракції (LibraryInterface), а не від конкретного класу Library
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.library.add(new_book)

    def remove_book(self, title):
        self.library.remove(title)

    def show_books(self):
        books = self.library.get_all()
        if not books:
            print("Library is empty.")
        for book in books:
            print(book)

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()