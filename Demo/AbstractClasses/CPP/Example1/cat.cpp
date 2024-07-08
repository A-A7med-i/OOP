#include "cat.h"
#include <string>
#include <iostream>

Cat::Cat(std::string n) : name(n)
{
}

void Cat::speak()
{
    std::cout << "Meow!" << std::endl;
}

std::string Cat::getName()
{
    return name;
}
