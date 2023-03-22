#include <iostream>
#include "cutlery.h"
using namespace std;

int main()
{
    cout << "Hello World!\n";
    cutlery nuclear(0);
    cutlery myname(1);
    cutlery eff(2);
    cutlery china(3);
    nuclear.printInfo();
    nuclear.use();
    nuclear.printInfo();
    nuclear.wash();
    nuclear.printInfo();
    myname.printInfo();
    myname.use();
    myname.printInfo();
    myname.wash();
    myname.printInfo();
    eff.printInfo();
    eff.use();
    eff.printInfo();
    eff.wash();
    eff.printInfo();
    china.printInfo();
    china.use();
    china.printInfo();
    china.wash();
    china.printInfo();

}
