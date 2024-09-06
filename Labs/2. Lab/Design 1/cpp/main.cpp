#include <iostream>

using namespace std;

class Point
{
public:
    double x, y, z;
    Point();
    Point(double x, double y, double z);
    void display();
    double calculateDistance(Point p);
};

Point::Point() : x(0), y(0), z(0)
{
}

Point::Point(double x, double y, double z) : x(x), y(y), z(z)
{
}

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

    Point p1(3, 4, 5);

    Point p2(6, 8, 10);

    p1.display();

    p2.display();

    cout << p1.calculateDistance(p2) << endl;

    Point p3;

    p3.display();

    cout << p3.calculateDistance(p2) << endl;

    return 0;
}