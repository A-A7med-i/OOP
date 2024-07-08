#include "myclass.h"
#include <iostream>

int MyClass::count = 0;

MyClass::MyClass()
{
    count++;
}

int MyClass::getCount()
{
    return count;
}

void MyClass::staticMehtod()
{
    std::cout << "Static Method" << std::endl;
}