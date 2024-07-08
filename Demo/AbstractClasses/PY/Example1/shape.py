from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Represents a geometric shape.
    """

    @abstractmethod
    def get_area(self):
        """
        Abstract method to calculate the area of the shape.
        This method must be implemented by derived classes.
        """
        pass

    def display(self):
        """This method provides the base shape display behavior."""
        print("This is a Shape object.")
