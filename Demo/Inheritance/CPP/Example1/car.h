#include "vehicle.h"
#include "engine.h"

class Car : public Vehicle, public Engine
{
private:
    int numDoors;

public:
    Car(std::string m, std::string c, int n, std::string f, int p, int nd);
    void setNumOfDoors(int newNum);
    int getNumOfDoors();
    void display();
};
