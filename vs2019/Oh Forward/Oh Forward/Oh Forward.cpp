#include <iostream>
using namespace std;
float Circumference(int radius);
int main()
{
    cout << "Oh Four Letter word.\n";
    int umm = 0;
    while (umm <= 33) {
        cout << umm << endl;
        umm += 5;
    }
    char would = 'n';
    while (would == 'y') {
        cout << "DONUT!\nWould you like to have another donut? (y/n)\n";
        cin >> would;
    }
    //Error: Undefined thing: do-while in brain space. Problem skipped.
    int radical = 0;
    while (radical != 69420) {
        cout << "Please enter a radius!1\n";
        cin >> radical;
        cout << "The Circumference of ur circle is " << Circumference(radical) << endl;
    }

}
float Circumference(int radius) {
    double pi = 3.14159265358;
    double tau = pi * 2;
    float circum = radius * tau;
    return circum;
}