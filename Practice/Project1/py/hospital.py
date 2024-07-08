from py.patient import Patient


class Hospital:
    """
    This class represents a hospital system with a single queue for patients.

    Attributes:
        patients (list): List of Patient objects waiting in the queue.
        max_patients (int): Maximum number of patients allowed in the queue.
    """

    def __init__(self):
        """
        Initializes the hospital system with an empty queue and a maximum patient limit.
        """
        self.patients = []
        self.max_patients = 5

    def menu(self):
        """
        Displays a menu with options for adding, printing, getting the next patient, and exiting.
        """
        print("Enter your choice:")
        print("1) Add new patient")
        print("2) Print all patients")
        print("3) Get next patient")
        print("4) Exit")

    def add_patient(self):
        """
        Adds a new patient to the queue if there's space, handling user input and potential errors.
        """
        if len(self.patients) < self.max_patients:
            try:
                specialization = int(input("Enter specialization (1-20): "))
                name = input("Enter patient name: ")
                status = int(input("Enter status (0 for regular, 1 for urgent): "))
                self.patients.append(Patient(specialization, name, status))
                print("Patient added successfully.")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        else:
            print("Queue is full.")

    def print_all_patients(self):
        """
        Prints information about all patients in the queue.
        """
        print(f"Total patients: {len(self.patients)}")
        for i, patient in enumerate(self.patients, start=1):
            print(f"Patient {i}:")
            print(f"  Name: {patient.name}")
            print(f"  Specialization: {patient.specialization}")
            print(f"  Status: {'urgent' if patient.status else 'regular'}")

    def get_next_patient(self):
        """
        Retrieves and displays information about the next patient in the queue.
        """
        if self.patients:
            next_patient = self.patients.pop(0)
            print("Next patient:")
            print(f"  Name: {next_patient.name}")
            print(f"  Specialization: {next_patient.specialization}")
            print(f"  Status: {'urgent' if next_patient.status else 'regular'}")
        else:
            print("No patients in the queue.")

    def loop(self):
        """
        Runs a continuous loop displaying the menu and handling user choices.
        """
        while True:
            self.menu()
            choice = input()
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.print_all_patients()
            elif choice == "3":
                self.get_next_patient()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
