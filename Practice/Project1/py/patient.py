class Patient:
    """
    This class represents a patient in a hospital system.

    Attributes:
        specialization (str): The patient's medical specialization (e.g., Pediatrics, Cardiology).
        name (str): The patient's name.
        status (int): The patient's status (0: Regular, 1: Urgent).
    """

    def __init__(self, specialization, name, status):
        self.specialization = specialization
        self.name = name
        self.status = status
