import logging
from abc import ABC, abstractmethod
from typing import List, Optional

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# SRP: Клас Book відповідає лише за зберігання даних про книгу 
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# ISP: Інтерфейс для роботи з бібліотекою 
class LibraryInterface(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

# OCP/LSP: Реалізація інтерфейсу 
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book added: {book.title}")

    def remove(self, title: str) -> None:
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < initial_count:
            logger.info(f"Book removed: {title}")
        else:
            logger.warning(f"Book not found: {title}")

    def get_all(self) -> List[Book]:
        return self.books

# DIP: Менеджер залежить від абстракції LibraryInterface 
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        new_book = Book(title, author, year)
        self.library.add(new_book)

    def remove_book(self, title: str) -> None:
        self.library.remove(title)

    def show_books(self) -> None:
        books = self.library.get_all()
        if not books:
            logger.info("Library is empty.")
            return
        
        logger.info("Current books in library:")
        for book in books:
            logger.info(str(book))

def main() -> None:
    library: LibraryInterface = Library()
    manager = LibraryManager(library)

    while True:
        command: str = input("\nEnter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting application.")
                break
            case _:
                logger.error("Invalid command. Please try again.") 

if __name__ == "__main__":
    main()