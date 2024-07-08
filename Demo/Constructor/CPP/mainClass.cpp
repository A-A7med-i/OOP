#include <iostream>
#include "person.h"

using namespace std;

int main()
{

    Person p1("Alice", 30);
    Person p2("Bob", 25);

    p1.display();
    p2.display();

    return 0;
}