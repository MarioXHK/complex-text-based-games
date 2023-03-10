#include <iostream>
using namespace std;
#include "pizza.h"

int main()
{
    pizza cheese;
    pizza law;
    pizza pineapple;
    pizza popeyes;
    pizza pop_pies;
    cheese.info();
    law.info();
    pineapple.info();
    popeyes.info();
    pop_pies.info();
    cout << "Time to do the baking and stuff.\n";
    cheese.addTopping(3);
    law.changemain("Pepperoni");
    law.addTopping(5);
    pineapple.changemain("Pineapple");
    pineapple.addTopping();
    popeyes.changemain("Cheddar");
    pop_pies.changemain("Mac n' Cheese");
    cheese.bake();
    law.bake();
    pineapple.bake();
    popeyes.bake();
    popeyes.bake();
    cheese.info();
    law.info();
    pineapple.info();
    popeyes.info();
    pop_pies.info();
    cout << "Oh, oops.\nI accidentally cooked the popeyes dish twice.\nWhy don't you make your own pizza?\nFirst, please say what kind of pizza you would like.\n";
    int top;
    string thing;
    pizza yours;
    cin >> thing;
    yours.changemain(thing);
    cout << "\nNow please tell me how many of this " << thing << " would you like on your pizza.\n";
    cin >> top;
    yours.addTopping(top);
    cout << "\nGreat, now to bake this and see what comes out.\n";
    yours.bake();
    yours.info();
    cout << "\nAh yes, this is indeed pizza time.\n";
    int totalprice = (cheese.price() + law.price() + pineapple.price() + popeyes.price() + pop_pies.price() + yours.price());
    cout << "Your total price for all these pizzas will be " << totalprice << " dollars.\n";
    if (totalprice > 0)
        cout << "Have a good day!\n";
    else
        cout << "Wait, how did you... do that?\n";
}