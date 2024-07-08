#include "patient.h"
#include <string>

Patient::Patient(std::string name, int specialization, int status)
    : specialization(specialization), name(name), status(status)
{
}

int Patient::getSpecialization()
{
    return specialization;
}

std::string Patient::getName()
{
    return name;
}

int Patient::getStatus()
{
    return status;
}
