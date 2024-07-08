#include "Invoice.h"
#include <iostream>
#include <string>

Invoice::Invoice(std::string name, int itemNumber, float price, int quantity)
    : name(name), itemNumber(itemNumber), price(price), quantity(quantity)
{
}

int Invoice::getItemNumber()
{
    return itemNumber;
}

void Invoice::setItemNumber(int newItemNumber)
{
}

std::string Invoice::getName()
{
    return name;
}

void Invoice::setName(std::string newName)
{
    name = newName;
}

float Invoice::getPrice()
{
    return price;
}

void Invoice::setPrice(float newPrice)
{
    price = newPrice;
}

int Invoice::getQuantity()
{
    return quantity;
}

void Invoice::setQuantity(int newQuantity)
{
    quantity = newQuantity;
}

double Invoice::getTotalPrice()
{
    return price * quantity;
}

void Invoice::print()
{
    std::cout << "Item Name: " << name << std::endl;
    std::cout << "Item Price: " << price << std::endl;
    std::cout << "Item Quantity: " << quantity << std::endl;
    std::cout << "Item item number: " << itemNumber << std::endl;
    std::cout << "Item Total Price: " << getTotalPrice() << std::endl;
}
