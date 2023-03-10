#pragma once
#include <iostream>
class pizza {
private:
    std::string topping;
    int toppings;
    bool isbaked;
    bool overbake;
public:
    pizza();
    void info();
    void addTopping(int amt = 1);
    void changemain(std::string top);
    void bake();
    int price();
};