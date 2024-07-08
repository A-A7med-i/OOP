#include <iostream>

using namespace std;

// Method Overriding

class Animal
{
public:
    virtual void speak() = 0;
};

class Dog : public Animal
{
private:
    string name;

public:
    Dog(string n) : name(n)
    {
    }
    void speak() override
    {
        cout << name << " says Woof!" << endl;
    }
};

class Cat : public Animal
{
private:
    string name;

public:
    Cat(string n) : name(n)
    {
    }
    void speak() override
    {
        cout << name << " says Meow!" << endl;
    }
};

// Function Overloading:

int add(int num1, int num2);

double add(double num1, double num2);

int main()
{
    Animal *animal1 = new Dog("Fido");     // Animal pointer referencing a Dog object
    Animal *animal2 = new Cat("Whiskers"); // Animal pointer referencing a Cat object

    animal1->speak();
    animal2->speak();

    delete animal1;
    delete animal2;

    cout << add(2, 3) << endl;

    cout << add(2.5, 3.5) << endl;
}

int add(int num1, int num2)
{
    return num1 + num2;
}

double add(double num1, double num2)
{
    return num1 + num2;
}
