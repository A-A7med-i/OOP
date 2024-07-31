from choice import (
    ChoiceOne,
    ChoiceTwo,
    ChoiceThree,
    ChoiceFour,
    ChoiceFive,
    ChoiceSix,
    ChoiceSeven,
    ChoiceEight,
)


class Main:
    """
    Main class for the Library System application.
    Handles the menu display and user interactions.
    """

    def __init__(self) -> None:
        """
        Initialize the Main class with a dictionary of choice objects.
        """
        self.choices = {
            1: ChoiceOne(),
            2: ChoiceTwo(),
            3: ChoiceThree(),
            4: ChoiceFour(),
            5: ChoiceFive(),
            6: ChoiceSix(),
            7: ChoiceSeven(),
            8: ChoiceEight(),
        }

    def menu(self) -> None:
        """
        Display the Library System menu options.
        """
        print("Library System Menu:", "1. Add Book", "2. Add User", sep="\n", end="\n")
        print(
            "3. List Books",
            "4. Find Borrowers by Book",
            sep="\n",
            end="\n",
        )
        print(
            "5. Borrow Book",
            "6. Return Book",
            "7. List Users",
            "8. Exit",
            sep="\n",
            end="\n",
        )

    def main(self) -> None:
        """
        The main loop that runs the library system menu and handles user interactions.
        Prompts for user input, executes the chosen action, and continues until the user chooses to exit.
        """
        while True:
            self.menu()

            try:
                choice = int(input("Enter The Choice\n"))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            if choice in self.choices:
                result = self.choices[choice].get_choice()
                if result is False:
                    break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
