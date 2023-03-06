//train simulator- shows basics of linked lists in C++
#include <iostream>
using namespace std;

void bobgood(bool good, string name);

class Goomba {
private:
    int xpos;
    int ypos;
    bool isAlive;
    char color;
    string name;
public:
    Goomba();
    Goomba(string chara, int x, int y, char rgb);
    void walk();
    void setPos(int x, int y);
    void printInfo();
    void kill();
    void recolor(char colour);
    bool CheckIsDead();
};


int main()
{
    Goomba Lary("Lary", 300, 400, 'l');
    Goomba Bob;
    Lary.printInfo();
    Lary.walk();
    Lary.printInfo();
    Bob.printInfo();
    Bob.setPos(500, 400);
    Bob.printInfo();
    Bob.walk();
    Lary.walk();
    Lary.printInfo();
    Bob.printInfo();
    Lary.walk();
    Lary.printInfo();
    Lary.recolor('B');
    Lary.printInfo();
    Lary.kill();
    Lary.printInfo();
    Bob.printInfo();
    bobgood(Lary.CheckIsDead(), "Bob");
    Lary.setPos(0, 0);
    bobgood(Lary.CheckIsDead(), "Bob");
    Lary.printInfo();
    Bob.walk();
    Bob.printInfo();
    Bob.recolor('r');
    Bob.printInfo();
    Bob.recolor('o');
    Bob.printInfo();
    Bob.recolor('y');
    Bob.printInfo();
    Bob.recolor('g');
    Bob.printInfo();
    Bob.recolor('l');
    Bob.printInfo();
    Bob.recolor('p');
    Bob.printInfo();
    Bob.recolor('0');
    Bob.printInfo();
    Bob.setPos(0, 0);
    Bob.recolor('b');
    Bob.printInfo();
    Lary.printInfo();
}

void bobgood(bool good, string name) {
    if (good)
        cout << name << " is happy :)\n";
    else
        cout << name << " is sad :(\n";
}


Goomba::Goomba() {
    name = "Bob";
    xpos = 0;
    ypos = 0;
    color = 'b';
    isAlive = false;
}
Goomba::Goomba(string chara, int x, int y, char rgb) {
    name = chara;
    xpos = x;
    ypos = y;
    color = rgb;
    isAlive = true;
}

void Goomba::walk() {
    cout << name << " walks.\n";
    xpos += 1;
}

void Goomba::setPos(int x, int y) {
    xpos = x;
    ypos = y;
    cout << name << " appears at " << xpos << ", " << ypos << " alive.\n";
    isAlive = true;
}


void Goomba::printInfo() {
    cout << "Hi, my name is " << name << ". I'm a goomba and my position is " << xpos << ", " << ypos << "\nMy color is ";
    switch (color) {
    case 'a':
        cout << "Amber";
        break;
    case 'b':
        cout << "Brown";
        break;
    case 'c':
        cout << "Cyan";
        break;
    case 'd':
        cout << "Black";
        break;
    case 'e':
        cout << "Euclid";
        break;
    case 'f':
        cout << "Infrared";
        break;
    case 'g':
        cout << "Green";
        break;
    case 'h':
        cout << "Hazel";
        break;
    case 'i':
        cout << "Indigo";
        break;
    case 'j':
        cout << "lime";
        break;
    case 'k':
        cout << "Clear";
        break;
    case 'l':
        cout << "Blue";
        break;
    case 'm':
        cout << "Magenta";
        break;
    case 'o':
        cout << "Orange";
        break;
    case 'p':
        cout << "Purple";
        break;
    case 'q':
        cout << "Opaque";
        break;
    case 'r':
        cout << "Red";
        break;
    case 's':
        cout << "Sausage";
        break;
    case 't':
        cout << "Teal";
        break;
    case 'u':
        cout << "Ultraviolet";
        break;
    case 'v':
        cout << "Violet";
        break;
    case 'w':
        cout << "Waffle Mix";
        break;
    case 'x':
        cout << "X-Ray";
        break;
    case 'y':
        cout << "Yellow";
        break;
    case 'z':
        cout << "Zellow";
        break;
    case '0':
        cout << "White";
        break;
    case '1':
        cout << "Gold";
        break;
    case '2':
        cout << "Silver";
        break;
    case '3':
        cout << "Bronze";
        break;
    case '4':
        cout << "Copper";
        break;
    case '5':
        cout << "Metal";
        break;
    case '6':
        cout << "Polygon";
        break;
    case '7':
        cout << "Cookie";
        break;
    case '8':
        cout << "Rust";
        break;
    case '9':
        cout << "Grey";
        break;
    case '"':
        cout << "Milk";
        break;
    case '\'':
        cout << "Chocolate milk";
        break;
    case '/':
        cout << "Gameboy";
        break;
    case '\\':
        cout << "Freedom";
        break;
    case '-':
        cout << "Color";
        break;
    case '=':
        cout << "Glow";
        break;
    case ';':
        cout << "Green and Black";
        break;
    case '`':
        cout << "Easter Egg";
        break;
    case '!':
        cout << "Blood";
        break;
    case '@':
        cout << "Rainbow";
        break;
    case '#':
        cout << "Flashing Colors";
        break;
    case '$':
        cout << "Greed";
        break;
    case '%':
        cout << "Paper";
        break;
    case '^':
        cout << "Cosmic Latte";
        break;
    case '&':
        cout << "Multiple types of Grey";
        break;
    case '*':
        cout << "Blue Screen";
        break;
    case '(':
        cout << "Microwave";
        break;
    case ')':
        cout << "Gamma";
        break;
    case '_':
        cout << "Transparent";
        break;
    case '+':
        cout << "Radiation";
        break;
    case '~':
        cout << "Pilk";
        break;
    case 'A':
        cout << "Aqua";
        break;
    case 'B':
        cout << "Bellow";
        break;
    case 'C':
        cout << "Japan";
        break;
    case 'D':
        cout << "Dlue";
        break;
    case 'E':
        cout << "EAS";
        break;
    case 'F':
        cout << "Flower";
        break;
    case 'G':
        cout << "Gron";
        break;
    case 'H':
        cout << "Scabby";
        break;
    case 'I':
        cout << "Light Grey";
        break;
    case 'J':
        cout << "Dark Grey";
        break;
    case 'K':
        cout << "Blood Stained";
        break;
    case 'L':
        cout << "Lava";
        break;
    case 'M':
        cout << "Medium Grey";
        break;
    case 'O':
        cout << "Oval";
        break;
    case 'P':
        cout << "Pink";
        break;
    case 'Q':
        cout << "Q";
        break;
    case 'R':
        cout << "Redder";
        break;
    case 'S':
        cout << "Stal";
        break;
    case 'T':
        cout << "To be determined";
        break;
    case 'U':
        cout << "Universal Constant";
        break;
    case 'V':
        cout << "Violent";
        break;
    case 'W':
        cout << "Double Ultraviolet";
        break;
    case 'X':
        cout << xpos;
        break;
    case 'Y':
        cout << ypos;
        break;
    case 'Z':
        cout << "Zenith";
        break;
    case ':':
        cout << "Ellow";
        break;
    case '.':
        cout << "Zed";
        break;
    case ',':
        cout << isAlive;
        break;
    case '[':
        cout << "Green^2";
        break;
    case ']':
        cout << "Speshle colur";
        break;
    case '{':
        cout << "Special Color";
        break;
    case '}':
        cout << "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
        break;
    case '|':
        cout << "Magenta and Black in a tile pattern";
        break;
    case '<':
        cout << "Glitchy";
        break;
    case '>':
        cout << "Number Lock";
        break;
    case '?':
        cout << "Random";
        break;
    case '\n':
        cout << "\\n";
        break;
    default:
        cout << "Something I don't know, I'm colorblind.";
        break;
    }
    cout << endl;
    if (isAlive)
        cout << "I am currently live\n";
    else
        cout << "I am dead.\n";
}

void Goomba::kill() {
    cout << "AAAA-\n";
    isAlive = false;
    cout << name << " has been killed.\n";
}

void Goomba::recolor(char colour) {
    cout << name << " has been recolored!\n";
    color = colour;
}

bool Goomba::CheckIsDead() {
    return isAlive;
}