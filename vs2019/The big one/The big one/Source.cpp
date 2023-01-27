//DEAR GOD AAAAAAAAAAAAAA
#include<iostream>
#include<math.h>
using namespace std;

double Snowdin(int stuff, int again);

class kyle {
private:
    int hunger;
    int tiredness;
    int boredom;
    int numberer;
public:
    kyle();
    kyle(int number);
    void eat();
    void playWarframe();
    void sleep();
    void work();
    void printing();
};//

int main() {
    string nothing;
    cout << "Here it comes!" << endl << endl << endl << "The big one..." << endl;
    //cin >> nothing;
    for (int i = 25; i <= 45; i++)
        cout << i << " ";
    cout << endl;
    for (int i = 90; i >= 70; i -= 2)
        cout << i << " ";
    cout << endl;
    for (int i = 10; i <= 5000; i *= 5)
        cout << i << " ";
    cout << endl;
    for (int i = 0; i <= 5; i++) {
        for (int j = 2; j <= 4; j++)
            cout << j << " ";
        cout << endl;
    }
    int cookies;
    cout << "How many cookies do you have?" << endl;
    cin >> cookies;
    if (cookies < 5)
        cout << "That seams like a few too little, mind if I give you some?" << endl;
    else if (cookies <= 10)
        cout << "That's a find amount of cookies you've got there!" << endl;
    else
        cout << "That's a lot of cookies......" << endl << endl << "G i v e ." << endl;
    char character;
    cout << "Who do you like best? \n(b)art simpson, (s)cooby doo, (r)ick, (d)affy duck, or (e)na?\n";
    cin >> character;
    if (character == 'b')
        cout << "Eat my shorts!" << endl;
    else if (character == 's')
        cout << "Scooby dooby doo!" << endl;
    else if (character == 'r')
        cout << "Wubba lubba dub dub!" << endl;
    else if (character == 'd')
        cout << "Sufferin' succotash..." << endl;
    else if (character == 'e')
        cout << "What conspiracies are we cooking on the menu today?" << endl;
    else
        cout << "That's not an option" << endl;
    cout << "I'm gonna ask you again, Who do you like best?" << endl << "(b)art simpson, (s)cooby doo, (r)ick, (d)affy duck, or (e)na?" << endl;
    cin >> character;
    switch (character) {
    case 'b':
        cout << "Eat my shorts!" << endl;
        break;
    case 's':
        cout << "Scooby dooby doo!" << endl;
        break;
    case 'r':
        cout << "Wubba lubba dub dub!!!" << endl;
        break;
    case 'd':
        cout << "Sufferin' succotash!" << endl;
        break;
    case 'e':
        cout << "YOU'RE ALL LIVING A LIE!!!" << endl;
        break;
    default:
        cout << "Wrong again, bucko..." << endl;
        break;
    }
    char ice;
    cout << "Would you like (i)ce cream or (c)andy?" << endl;
    cin >> ice;
    char side;
    cout << "(c)hocolate or (f)ruit?" << endl;
    cin >> side;
    if (ice == 'i')
        if (side == 'c')
            cout << "Here's a hot fudge sundae!" << endl;
        else if (side == 'f')
            cout << "Here's a strawberry blizzard!" << endl;
        else
            cout << "Here's an Ice Cream Snowgrave!" << endl;
    else if (ice == 'c')
        if (side == 'c')
            cout << "Have a Hershy bar!" << endl;
        else if (side == 'f')
            cout << "Here's some fruit gummies!" << endl;
        else
            cout << "Here's 5 grams of pure sugar." << endl;
    else
        if (side == 'c')
            cout << "Here's some white chocolate!" << endl;
        else if (side == 'f')
            cout << "Giving you a Grape." << endl;
        else
            cout << "..." << endl;
    int ay;
    int bee;
    cout << "What is your A number?\n";
    cin >> ay;
    cout << "What is your B number?\n";
    cin >> bee;
    double see = Snowdin(ay, bee);
    cout << "Your C is " << see << endl;
    cout << "Now anyways it's time to activate the apocalypse.\n";
    kyle mia(1);
    kyle sonic(2);
    kyle frypan(3);
    kyle og(0);
    cout << "4 Kyles have spawned in the area\n";
    bool death = true;
    char health;
    char option = 'f';
    while (death) {
        og.printing();
        mia.printing();
        sonic.printing();
        frypan.printing();
        cout << "Choose which Kyle to interact with." << endl;
        cin >> health;
        switch (health) {
        case '0':
            cout << "What would you like to do with the Orignal Kyle?" << endl << "(e)at, (s)leep, (p)lay, or (w)ork?" << endl;
            cin >> option;
            switch (option) {
            case 'e':
                og.eat();
                break;
            case 's':
                og.sleep();
                break;
            case 'p':
                og.playWarframe();
                break;
            case 'w':
                og.work();
                break;
            case 'q':
                cout << "Goodbye.\n";
                break;
            default:
                cout << "That is not an option\n";
            }
            break;
        case '1':
            cout << "What would you like to do with the Mia Kyle?" << endl << "(e)at, (s)leep, (p)lay, or (w)ork?" << endl;
            cin >> option;
            switch (option) {
            case 'e':
                mia.eat();
                break;
            case 's':
                mia.sleep();
                break;
            case 'p':
                mia.playWarframe();
                break;
            case 'w':
                mia.work();
                break;
            case 'q':
                cout << "Goodbye.\n";
                break;
            default:
                cout << "That is not an option\n";
            }
            break;
        case '2':
            cout << "What would you like to do with the Sonic fan Kyle?" << endl << "(e)at, (s)leep, (p)lay, or (w)ork?" << endl;
            cin >> option;
            switch (option) {
            case 'e':
                sonic.eat();
                break;
            case 's':
                sonic.sleep();
                break;
            case 'p':
                sonic.playWarframe();
                break;
            case 'w':
                sonic.work();
                break;
            case 'q':
                cout << "Goodbye.\n";
                break;
            default:
                cout << "That is not an option\n";
            }
            break;
        case '3':
            cout << "What would you like to do with the Cooking Kyle?" << endl << "(e)at, (s)leep, (p)lay, or (w)ork?" << endl;
            cin >> option;
            switch (option) {
            case 'e':
                frypan.eat();
                break;
            case 's':
                frypan.sleep();
                break;
            case 'p':
                frypan.playWarframe();
                break;
            case 'w':
                frypan.work();
                break;
            case 'q':
                cout << "Goodbye.\n";
                break;
            default:
                cout << "That is not an option\n";
            }
            break;
        case 'q':
            cout << "Goodbye." << endl;
            option = 'q';
            break;
        default:
            cout << "There is no Kyle with that number, try again!\n";
            break;
        
        }
        if (option == 'q')
            death = true;
    }
}

double Snowdin(int stuff, int again) {
    int a = stuff * stuff;
    int b = again * again;
    double c = sqrt(a + b);
    return c;
}

kyle::kyle() {
    hunger = 0;
    tiredness = 0;
    boredom = 0;
    numberer = 0;
}

kyle::kyle(int number) {
    hunger = 0;
    tiredness = 0;
    boredom = 0;
    numberer = number;
}

void kyle::eat() {
    hunger -= 10;
    cout << "Yummeh cake!1\n";
}

void kyle::playWarframe() {
    boredom -= 10;
    cout << "https://tvtropes.org/pmwiki/pmwiki.php/Quotes/Warframe" << endl;
}

void kyle::sleep() {
    tiredness -= 10;
    cout << "zzz\n";
}

void kyle::work() {
    hunger += 10;
    tiredness += 10;
    boredom += 10;
    cout << "Aauughh...\n";
}

void kyle::printing() {
    cout << "This is kyle " << numberer << ". It has " << hunger << " hunger, " << tiredness << " tiredness, and " << boredom << " boredom." << endl;
}