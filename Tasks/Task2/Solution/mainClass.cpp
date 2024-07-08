#include "cpp\Invoice.h"
#include <iostream>

using namespace std;

int main()
{
    // Create an Invoice object with valid parameters
    Invoice myInvoice("Computer Mouse", 1234, 19.99, 2);

    // Test the print function to display invoice details
    myInvoice.print();

    return 0;
}