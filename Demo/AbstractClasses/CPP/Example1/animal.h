#include <string>

// We initialize functions with = 0 in C++ to declare them as pure virtual functions,
// also known as abstract methods.

class Animal
{
public:
    virtual void speak() = 0;
    virtual std::string getName() = 0;
    virtual void display() final;
};
