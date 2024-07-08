#include "dog.h"
#include <iostream>
#include <string>

Dog::Dog(std::string n) : name(n)
{
}

void Dog::speak()
{
    std::cout << "Woof!" << std::endl;
}

std::string Dog::getName()
{
    return name;
}
