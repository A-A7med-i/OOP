#include "hospital.h"
#include "patient.h"
#include <iostream>

using namespace std;

Hospital::Hospital()
{
    max_patients = 5;
}

void Hospital::menu()
{
    cout << "Enter your choice:" << endl
         << "1) Add new patient" << endl
         << "2) Print all patients" << endl
         << "3) Get next patient" << endl
         << "4) Exit" << endl;
}

void Hospital::addPatient()
{
    int specialization;
    string name;
    int status;

    if (patients.size() < max_patients)
    {
        cout << "Enter specialization (1-20): " << endl;
        cin >> specialization;
        cout << "Enter patient name: " << endl;
        cin >> name;
        cout << "Enter status (0 for regular, 1 for urgent): " << endl;
        cin >> status;
        patients.push_back(Patient(name, specialization, status));
        cout << "Patient added successfully." << endl;
    }

    else
    {
        cout << "Queue is full." << endl;
    }
}

void Hospital::printAllPatients()
{
    if (patients.empty())
    {
        cout << "No patients in the queue." << endl;
        return;
    }

    cout << "Total patients: " << patients.size() << endl;
    for (size_t i = 0; i < patients.size(); ++i)
    {
        Patient &patient = patients[i];
        cout << "Patient " << (i + 1) << ":" << endl;
        cout << "  Name: " << patient.getName() << endl;
        cout << "  Specialization: " << patient.getSpecialization() << endl;
        cout << "  Status: " << (patient.getStatus() == 1 ? "urgent" : "regular") << endl;
    }
}

void Hospital::getNextPatient()
{
    if (patients.empty())
    {
        cout << "No patients in the queue." << endl;
        return;
    }
    Patient nextPatient = patients[0];
    patients.erase(patients.begin());
    cout << "Next patient:" << endl;
    cout << "  Name: " << nextPatient.getName() << endl;
    cout << "  Specialization: " << nextPatient.getSpecialization() << endl;
    cout << "  Status: " << (nextPatient.getStatus() == 1 ? "urgent" : "regular") << endl;
}

void Hospital::loop()
{
    while (true)
    {
        menu();
        char choice;
        cin >> choice;
        switch (choice)
        {
        case '1':
            addPatient();
            break;
        case '2':
            printAllPatients();
            break;
        case '3':
            getNextPatient();
            break;
        case '4':
            return;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    }
}
