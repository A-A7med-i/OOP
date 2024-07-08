#include "car.h"
#include <iostream>

Car::Car(std::string m, std::string c, int n, std::string f, int p, int nd)
    : Vehicle(m, c, n), Engine(f, p), numDoors(nd)
{
}

void Car::setNumOfDoors(int newNum)
{
    numDoors = newNum;
}

int Car::getNumOfDoors()
{
    return numDoors;
}

void Car::display()
{
    Vehicle::display();
    Engine::display();
    std::cout << "Number of Doors: " << numDoors << std::endl;
}
