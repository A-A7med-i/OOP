#include <vector>
#include "patient.h"

class Hospital
{
private:
    int max_patients;
    std::vector<Patient> patients;

public:
    Hospital();
    void menu();
    void addPatient();
    void printAllPatients();
    void getNextPatient();
    void loop();
};