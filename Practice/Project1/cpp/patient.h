#include <string>

class Patient
{
private:
    int specialization;
    std::string name;
    int status;

public:
    Patient(std::string name, int specialization, int status);
    int getSpecialization();
    std::string getName();
    int getStatus();
};