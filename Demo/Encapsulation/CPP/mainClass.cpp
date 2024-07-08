#include <iostream>
#include "point.h"

int main()
{

    point p(3, 4);
    int d = p.getDistancefromOrigin();

    std::cout << "The Distance from Origin Is: " << d << std::endl;

    p.setFirstPoint(5);

    d = p.getDistancefromOrigin();

    std::cout << "The Distance from Origin Is: " << d << std::endl;

    return 0;
}