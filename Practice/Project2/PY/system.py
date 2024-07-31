from book import Book
from user import User


class LibrarySystem:
    """
    A class representing a library system that manages books and users.

        This library system allows users to add books, users, list books, find borrowers
        by book, borrow books, return books, list users, and exit the program.

        Attributes:
            books (dict[int, Book]): A dictionary mapping book IDs to Book objects.
            users (dict[int, User]): A dictionary mapping user IDs to User objects.
    """

    def __init__(self) -> None:
        """Initializes the library system with empty dictionaries for books and users."""
        self.books: dict[int, Book] = {}
        self.users: dict[int, User] = {}

    def added_book(self, new_book: Book) -> None:
        """Adds a new book to the library system, handling duplicate ID checks.

        Args:
            new_book (Book): The Book object to be added.

        Raises:
            ValueError: If the book ID already exists and the book has a name.
        """

        if new_book.get_id() in self.books and new_book.get_name():
            print(
                f"A book with the ID {new_book.get_id()} already exists in the library."
            )
            return

        else:
            self.books[new_book.get_id()] = new_book
            print(
                f"Book '{new_book.name}' (ID: {new_book.get_id()}) added successfully!"
            )

    def added_user(self, new_user: User) -> None:
        """Adds a new user to the library system, handling duplicate ID checks.

        Args:
            new_user (User): The User object to be added.

        Raises:
            ValueError: If the user ID already exists.
        """

        if new_user.get_id() in self.users:
            print(
                f"A user with the ID {new_user.get_id()} already exists in the library."
            )
            return

        else:
            self.users[new_user.get_id()] = new_user
            print(
                f"User '{new_user.name}' (ID: {new_user.get_id()}) added successfully!"
            )

    def list_books(self, sorted_by: str = "id") -> list[Book]:
        """Lists books in the library, optionally sorted by ID or name.

        Args:
            sorted_by (str, optional): Sorting criteria. Defaults to "id".
                Valid options are "id" and "name".

        Returns:
            list[Book]: A list of Book objects sorted according to the provided criteria.

        Raises:
            ValueError: If the provided sorting option is invalid.
        """

        books = self.books.values()

        if sorted_by == "id":
            return sorted(books, key=lambda book: book.id)

        elif sorted_by == "name":
            return sorted(books, key=lambda book: book.name)

        else:
            print("Invalid sorting option")

    def find_borrowers_by_book_name(self, book_name: str) -> list[int]:
        """Finds the user IDs of borrowers for a given book name.

        Args:
            book_name (str): The name of the book to find borrowers for.

        Returns:
            list[int]: A list of user IDs of borrowers for the specified book.
                Returns an empty list if no borrowers are found.
        """

        borrowers = []

        for book in self.books.values():
            if book.name == book_name.strip():
                borrowers.extend(book.borrowed_by)

        return list(set(borrowers))

    def borrow_book(self, user_id: int, book_id: int) -> None:
        """Borrows a book for a user if available.

        Args:
            user_id (int): The ID of the user borrowing the book.
            book_id (int): The ID of the book to be borrowed.

        Raises:
            ValueError: If the user ID or book ID is invalid, or if the book is not available.
        """

        if user_id not in self.users:
            print("Invalid user ID")
            return

        if book_id not in self.books:
            print("Invalid book ID")
            return

        book = self.books[book_id]

        if book.quantity == 0:
            print("Book is not available")
            return

        book.quantity -= 1
        book.borrowed_by.append(user_id)
        self.users[user_id].borrowed_books.append(book_id)

        print(f"Book '{book.name}' borrowed successfully")

    def return_book(self, user_id: int, book_id: int) -> None:
        """Returns a borrowed book.

        Args:
            user_id (int): The ID of the user returning the book.
            book_id (int): The ID of the book to be returned.

        Raises:
            ValueError: If the user ID or book ID is invalid, or if the user hasn't
                borrowed the book.
        """

        if user_id not in self.users:
            print("Invalid user ID")
            return

        if book_id not in self.books:
            print("Invalid book ID")
            return

        book = self.books[book_id]
        book.quantity += 1
        book.borrowed_by.remove(user_id)
        self.users[user_id].borrowed_books.remove(book_id)
        print(f"Book '{book.name}' returned successfully")

    def list_users(self, sorted_by: str = "id") -> list[Book]:
        """Lists books in the library, optionally sorted by ID or name.

        Args:
            sorted_by (str, optional): Sorting criteria. Defaults to "id".
                Valid options are "id" and "name".

        Returns:
            list[Book]: A list of Book objects sorted according to the provided criteria.

        Raises:
            ValueError: If the provided sorting option is invalid.
        """

        users = self.users.values()

        if sorted_by == "id":
            return sorted(users, key=lambda user: user.id)

        elif sorted_by == "name":
            return sorted(users, key=lambda user: user.name)

        else:
            print("Invalid Option.")
            return
