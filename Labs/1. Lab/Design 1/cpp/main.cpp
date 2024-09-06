#include <iostream>
#include <cmath>

using namespace std;

class Point
{
public:
    double x, y, z;
    void display();
    double calculateDistance(Point p);
};

void Point::display()
{
    cout << "Point: " << "(" << x << "," << y << "," << z << ")" << endl;
}

double Point::calculateDistance(Point p)
{
    double distance = abs(x - p.x);
    return distance;
}

int main()
{

    Point p1;
    p1.x = 3, p1.y = 4, p1.z = 5;

    Point p2;
    p2.x = 6, p2.y = 8, p2.z = 10;

    p1.display();

    p2.display();

    cout << p1.calculateDistance(p2) << endl;

    return 0;
}
