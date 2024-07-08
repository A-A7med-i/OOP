#include "Example1\car.h"
#include <iostream>

using namespace std;

int main()
{

    Car c1("Tesla", "RED", 2019, "Electric", 420, 4);

    c1.display();
    // output:
    // Maker: Tesla
    // Color : RED
    // Model Year : 2019
    // Fuel Type : Electric
    // Horsepower : 420 HP
    // Number of Doors : 4

    return 0;
}