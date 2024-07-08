from Example1.person import Person


class Student(Person):
    """
    Represents a student who inherits attributes from the Person class
    and adds additional attributes specific to student information.

    Attributes:
        gpa (float): The student's grade point average.
        depart (str): The student's department.

    Inherits from:
        Person
    """

    def __init__(self, name: str, age: int, gpa: float, depart: str) -> None:
        """
        Initializes a Student object with basic information and academic details.

        Args:
            name (str): The student's name (inherited from Person).
            age (int): The student's age (inherited from Person).
            gpa (float): The student's grade point average.
            depart (str): The student's department.

        Raises:
            TypeError: If either gpa or depart is not of the expected type (float or str).
        """
        super().__init__(name, age)
        self.gpa = gpa
        self.depart = depart
        print("From Student")

    def set_gpa(self, new_gpa: float) -> None:
        """
        Updates the student's grade point average.

        Args:
            new_gpa (float): The new GPA value for the student.

        Raises:
            TypeError: If the new_gpa argument is not a floating-point number.
        """
        self.gpa = new_gpa

    def get_gpa(self) -> float:
        """
        Returns the student's current grade point average.

        Returns:
            float: The student's GPA.
        """
        return self.gpa

    def set_depart(self, new_depart: str) -> None:
        """
        Updates the student's department.

        Args:
            new_depart (str): The new department name for the student.

        Raises:
            TypeError: If the new_depart argument is not a string.
        """
        self.depart = new_depart

    def get_depart(self) -> str:
        """
        Returns the student's current department.

        Returns:
            str: The student's department name.
        """
        return self.depart

    def display(self) -> None:
        """
        Prints a greeting message including the inherited information from Person
        and the student's GPA and department.
        """
        super().display()  # Call the Person's display method
        print(f"Your gpa is : {self.gpa} and Your department is: {self.depart}")
