#include "animal.h"
#include <string>

class Cat : public Animal
{
private:
    std::string name;

public:
    Cat(std::string n);
    void speak();
    std::string getName();
};