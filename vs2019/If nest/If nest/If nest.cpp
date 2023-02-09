#include <iostream>
using namespace std;

int main()
{
    cout << "Let's pretend gates don't exist.\nAnyways, do you like platfomers? (y/n)\n";
    char plat;
    cin >> plat;
    cout << "What difficulty rating would you like yourself to experience? (1-10)\n";
    int hell;
    cin >> hell;
    if (hell <= 5) {
        if (plat == 'y')
            cout << "You should try Kirby's Epic Yarn.\n";
        else
            cout << "You should try Minecraft!\n";
    }
    else if (hell <= 10) {
        if (plat == 'y')
            cout << "You should play Super Mario Bros.\n";
        else
            cout << "You should play Half-Life.\n";
    }
    else if (hell <= 100) {
        if (plat == 'y')
            cout << "You should play Celeste!\n";
        else
            cout << "You should play Dark Souls!\n";
    }
    else {
        if (plat == 'y')
            cout << "You should play I wanna be the guy!\n";
        else
            cout << "You should play Flappy Bird!\n";
    }
}
