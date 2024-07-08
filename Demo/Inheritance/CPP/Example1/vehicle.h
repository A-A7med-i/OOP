#include <string>

class Vehicle
{
private:
    std::string maker;
    std::string color;
    int model;

public:
    Vehicle(std::string m, std::string c, int n);
    void setColor(std::string newColor);
    std::string getColor();
    void setMaker(std::string newMaker);
    std::string getMaker();
    void setModel(int new_model);
    int getModel();
    void display();
};