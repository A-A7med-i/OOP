#include <string>

class Invoice
{
private:
    std::string name;
    int itemNumber;
    float price;
    int quantity;

public:
    Invoice(std::string name, int itemNumber, float price, int quantity);
    int getItemNumber();
    void setItemNumber(int newItemNumber);
    std::string getName();
    void setName(std::string newName);
    float getPrice();
    void setPrice(float newPrice);
    int getQuantity();
    void setQuantity(int newQuantity);
    double getTotalPrice();
    void print();
};