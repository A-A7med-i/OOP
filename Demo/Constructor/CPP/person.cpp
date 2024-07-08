#include "person.h"
#include <string>
#include <iostream>

Person::Person(std::string n, int a) : name(n), age(a)
{
}

void Person::display()
{
    std::cout << "Hello, my name is " << name << " and I'm " << age << " years old." << std::endl;
}

Person::~Person()
{
    std::cout << "Deconstructor" << std::endl;
}
