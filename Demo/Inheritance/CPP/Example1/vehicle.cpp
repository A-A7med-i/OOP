#include "vehicle.h"
#include <iostream>

Vehicle::Vehicle(std::string m, std::string c, int n)
    : maker(m), color(c), model(n)
{
}

void Vehicle::setColor(std::string newColor)
{
    color = newColor;
}

std::string Vehicle::getColor()
{
    return color;
}

void Vehicle::setMaker(std::string newMaker)
{
    maker = newMaker;
}

std::string Vehicle::getMaker()
{
    return maker;
}

void Vehicle::setModel(int new_model)
{
    model = new_model;
}

int Vehicle::getModel()
{
    return model;
}

void Vehicle::display()
{
    std::cout << "Maker: " << maker << std::endl;
    std::cout << "Color: " << color << std::endl;
    std::cout << "Model Year: " << model << std::endl;
}
