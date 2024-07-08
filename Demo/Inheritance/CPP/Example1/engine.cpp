#include "engine.h"
#include <iostream>

Engine::Engine(std::string f, int p)
    : fuel_type(f), horsepower(p)
{
}

void Engine::setFuelType(std::string newFuel)
{
    fuel_type = newFuel;
}

std::string Engine::getFuelType()
{
    return fuel_type;
}

void Engine::setHorsePower(int newPower)
{
    horsepower = newPower;
}

int Engine::getHorsePower()
{
    return horsepower;
}

void Engine::display()
{
    std::cout << "Fuel Type: " << fuel_type << std::endl;
    std::cout << "Horsepower: " << horsepower << " HP" << std::endl;
}
