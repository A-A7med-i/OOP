from Example1.student import Student


class HighStudent(Student):
    """
    Represents a high school student with additional attributes and methods
    specific to their research involvement.

    Attributes:
        research (str): The research topic or area the student is involved in.

    Inherits from:
        Student
    """

    def __init__(
        self, name: str, age: int, gpa: float, depart: str, research: str
    ) -> None:
        """
        Initializes a HighStudent object with basic information and research area.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            gpa (float): The student's GPA.
            depart (str): The student's department.
            research (str): The student's research topic or area.

        Raises:
            TypeError: If any of the arguments except `research` are not of the
                        expected types (str, int, or float).
        """

        super().__init__(name, age, gpa, depart)
        self.research = research
        print("From High Student")  # Consider removing or modifying this

    def set_research(self, new_research: str) -> None:
        """
        Updates the student's research area.

        Args:
            new_research (str): The new research topic or area for the student.

        Raises:
            TypeError: If the new_research argument is not a string.
        """
        self.research = new_research

    def get_research(self) -> str:
        """
        Returns the student's current research area.

        Returns:
            str: The student's research topic or area.
        """

        return self.research

    def display(self) -> None:
        """
        Displays the student's information and research area.

        Prints the inherited student information and then adds the research area.
        """

        super().display()
        print(f"Research is: {self.research}")
