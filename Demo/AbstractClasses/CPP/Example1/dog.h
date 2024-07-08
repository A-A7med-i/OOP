#include "animal.h"
#include <string>

class Dog : public Animal
{
private:
    std::string name;

public:
    Dog(std::string n);
    void speak();
    std::string getName();
};
