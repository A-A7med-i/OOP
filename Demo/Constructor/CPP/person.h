#include <string>

class Person
{
private:
    std::string name;
    int age;

public:
    Person(std::string n, int a);
    void display();
    ~Person();
};