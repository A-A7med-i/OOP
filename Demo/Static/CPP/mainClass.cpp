#include <iostream>
#include "Example1\counter.h"
#include "Example2\mathutils.h"
#include "Example3\myclass.h"

using namespace std;

int main()
{
    Counter c1;
    Counter c2;
    Counter c3;

    cout << c3.getCount() << endl; // 3

    // if count not static the output is 1

    int mx = MathUtils::max(3, 4);

    cout << mx << endl; // 4

    MyClass m1;
    MyClass m2;
    MyClass m3;

    cout << m3.getCount() << endl;

    // error count is a private member
    // cout << MyClass::count << endl;

    m3.staticMehtod();

    MyClass::staticMehtod();

    return 0;
}
