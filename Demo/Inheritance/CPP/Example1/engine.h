#include <string>

class Engine
{
private:
    std::string fuel_type;
    int horsepower;

public:
    Engine(std::string f, int p);
    void setFuelType(std::string newFuel);
    std::string getFuelType();
    void setHorsePower(int newPower);
    int getHorsePower();
    void display();
};