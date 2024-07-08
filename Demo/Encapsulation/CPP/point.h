class point
{
private:
    int x;
    int y;

public:
    point(int firstPoint, int secondPoint);
    void setFirstPoint(int p);
    void setSecondPoint(int p);
    int getFirstPoint();
    int getSecondPoint();
    int getDistancefromOrigin();
};