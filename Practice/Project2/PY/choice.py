from typing import List
from abc import ABC, abstractmethod
from system import LibrarySystem
from book import Book
from user import User


class Choice(ABC):
    """
    Abstract base class for representing user choices in the library system.
    """

    @abstractmethod
    def get_choice(self):
        """
        Abstract method to be implemented by concrete choice classes.
        Handles the specific action associated with the choice.
        """
        pass


class ChoiceOne(Choice, LibrarySystem):
    """
    Represents the choice to add a new book to the library system.
    """

    def get_choice(self) -> None:
        """
        Prompts the user for book details (ID, name, quantity) and adds the book to the system.
        """
        id: int = int(input("Id: "))
        name: str = input("Name: ")
        quantity: int = int(input("quantity: "))
        self.added_book(Book(id, name, quantity))


class ChoiceTwo(Choice, LibrarySystem):
    """
    Represents the choice to add a new user to the library system.
    """

    def get_choice(self) -> None:
        """
        Prompts the user for user details (ID, name) and adds the user to the system.
        """
        id: int = int(input("Id: "))
        name: str = input("Name: ")
        self.added_user(User(id, name))


class ChoiceThree(Choice, LibrarySystem):
    """
    Represents the choice to list all books in the library system.
    """

    def get_choice(self) -> None:
        """
        Retrieves and displays a list of all books, including their details and borrowing status.
        """
        books: List[Book] = self.list_books()
        for book in books:
            print(
                f"- {book.id}: {book.name} (Quantity: {book.quantity}) total borrowed {len(book.borrowed_by)}"
            )


class ChoiceFour(Choice, LibrarySystem):
    """
    Represents the choice to find borrowers of a specific book by its name.
    """

    def get_choice(self) -> None:
        """
        Prompts the user for a book name and displays a list of users who have borrowed that book.
        """
        book_name: str = input("Enter book name: ")
        users: List[int] = self.find_borrowers_by_book_name(book_name)

        if not users:
            print(f"No users have borrowed '{book_name}'.")
            return

        print(f"Users who borrowed '{book_name}':")
        for user_id in users:
            user: User = self.users[user_id]
            print(f"- ID: {user.id} Name: {user.name}")


class ChoiceFive(Choice, LibrarySystem):
    """
    Represents the choice to borrow a book by a user.
    """

    def get_choice(self) -> None:
        """
        Prompts the user for user ID and book ID, then processes the borrowing action.
        """
        user_id: int = int(input("User ID: "))
        book_id: int = int(input("Book ID: "))
        self.borrow_book(user_id, book_id)


class ChoiceSix(Choice, LibrarySystem):
    """
    Represents the choice to return a book by a user.
    """

    def get_choice(self) -> None:
        """
        Prompts the user for user ID and book ID, then processes the book return action.
        """
        user_id: int = int(input("User ID: "))
        book_id: int = int(input("Book ID: "))
        self.return_book(user_id, book_id)


class ChoiceSeven(Choice, LibrarySystem):
    """
    Represents the choice to list all users in the library system.
    """

    def get_choice(self) -> None:
        """
        Retrieves and displays a list of all users along with their IDs.
        """
        users: List[User] = self.list_users()
        for user in users:
            print(f"- ID: {user.id}, Name: {user.name}")


class ChoiceEight(Choice):
    """
    Represents the choice to exit the library system.
    """

    def get_choice(self) -> bool:
        """
        Displays an exit message and returns False to signal the program to terminate.
        """
        print("Exiting the library system. Goodbye!")
        return False
