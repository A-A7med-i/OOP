#include "point.h"
#include <cmath>

point::point(int firstPoint, int secondPoint) : x(firstPoint), y(secondPoint)
{
}

void point::setFirstPoint(int p)
{
    x = p;
}

void point::setSecondPoint(int p)
{
    y = p;
}

int point::getFirstPoint()
{
    return x;
}

int point::getSecondPoint()
{
    return y;
}

int point::getDistancefromOrigin()
{
    return sqrt(pow(x, 2) + pow(y, 2));
}
