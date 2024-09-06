#include <iostream>

using namespace std;

/**
 * @brief Represents a fraction with numerator and denominator.
 *
 * This class provides basic operations for fractions, including
 * addition and display functionality.
 */

class Fraction
{
private:
    int denominator;

public:
    int numerator;

    void setDenominator(int newDenominator);

    int getDenominator();

    void display();

    void add(Fraction &f);
};

void Fraction::setDenominator(int newDenominator)
{
    if (newDenominator == 0)
        throw invalid_argument("Denominator cannot be zero");

    denominator = newDenominator;
}

int Fraction::getDenominator()
{
    return denominator;
}

void Fraction::display()
{
    cout << numerator << "/" << denominator << endl;
}

void Fraction::add(Fraction &f)
{
    int num = (this->numerator * f.getDenominator()) + (this->denominator * f.numerator);
    int den = this->denominator * f.getDenominator();

    cout << num << "/" << den << endl;
}

int main()
{

    Fraction f1;

    f1.numerator = 3;
    f1.setDenominator(4);

    Fraction f2;
    f2.numerator = 6;
    f2.setDenominator(8);

    f1.display();
    f2.display();

    cout << f1.getDenominator() << endl;

    // Error
    // f1.setDenominator(0);
    // cout << f1.getDenominator() << endl;

    f1.setDenominator(2);
    cout << f1.getDenominator() << endl;

    f1.add(f2);

    return 0;
}
