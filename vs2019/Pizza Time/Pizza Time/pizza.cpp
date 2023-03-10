#include "pizza.h"
#include <iostream>
using namespace std;

pizza::pizza() {
    toppings = 0;
    isbaked = false;
    topping = "Cheese";
    overbake = false;
}
void pizza::changemain(string top) {
    topping = top;
}
int pizza::price() {
    if (isbaked)
        return (toppings * 2) + 10;
    else
        return toppings + 6;
}
void pizza::bake() {
    if (!isbaked)
        isbaked = true;
    else
        overbake = true;
}
void pizza::addTopping(int amt) {
    toppings += amt;
}
void pizza::info() {
    cout << "This is a " << topping << " Pizza with " << toppings << " topping(s)\nIt's ";
    if (!isbaked)
        cout << "not ";
    if (overbake)
        cout << "over";
    cout << "baked, and the price is " << price() << " Dollars.\n";
}