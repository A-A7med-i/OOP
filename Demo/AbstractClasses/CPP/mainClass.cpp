#include <iostream>
#include "Example1\animal.h"
#include "Example1\cat.h"
#include "Example1\dog.h"

int main()
{

    Cat c("Whiskers");

    c.display();
    cout << c.getName() << endl;
    c.speak();

    cout << "##########" << endl;

    Dog d("Fido");

    d.display();
    cout << d.getName() << endl;
    d.speak();

    return 0;
}