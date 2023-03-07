#include <iostream>
using namespace std;

class Planet {
private:
    string name;
    double mass;
    int moons;
    int rings;
    char type;
    bool life;
public:
    Planet();
    Planet(string naem, double emass, int moony, int roche, char thing, bool living);
    void Aquire();
    void Shred();
    void Growlife();
    void Voidlife();
    void Print();
};

int main()
{
    Planet goo("Lena", 333333, 0, 5, 's', false);
    Planet zezt("Maddy", 125000,0,0,'l', false);
    Planet hell("Venal", 0.9, 0, 0, 'j', false);
    Planet earth;
    Planet terrar("Terrest", 1.1, 0, 1, 'r', false);
    Planet ether("Ether", 0.6, 2, 0, 'l', true);
    Planet guard("Guard", 13, 42, 7, 'g', false);
    Planet ola("Molah", 15, 6, 3, 'g', false);
    Planet plu("Pluto", 0.1, 1, 0, 'z', true);
    Planet pen("Pencil", 0.5, 0, 1, 'i', false);
    Planet dwarf("Simon", 0.2, 0, 1, 'z', true);
    goo.Print();
    zezt.Print();
    hell.Print();
    earth.Print();
    hell.Print();
    terrar.Print();
    ether.Print();
    guard.Print();
    ola.Print();
    plu.Print();
    pen.Print();
    dwarf.Print();
}

Planet::Planet() {
    name = "Earth";
    mass = 1.0;
    moons = 1;
    rings = 1;
    type = 'r';
    life = true;
}
Planet::Planet(string naem, double emass, int moony, int roche, char thing, bool living) {
    name = naem;
    mass = emass;
    moons = moony;
    rings = roche;
    type = thing;
    life = living;
}
void Planet::Aquire() {
    cout << "Oh cool, a moon appeared on " << name << endl;
    moons++;
}
void Planet::Shred() {
    if (moons > 0) {
        cout << "One of " << name << "'s moons reached the Roche limit and turned into a ring.\n";
        moons--;
        rings++;
    }
    else 
        cout << "There are no moons available for " << name << " to destroy.\n";
}
void Planet::Growlife() {
    if (!life) {
        cout << "Life is made on " << name << endl;
        life = true;
    }
    else
        cout << "Life evolves on " << name << endl;
}
void Planet::Voidlife() {
    if (life) {
        cout << "Life is destroyed.\n";
        life = false;
    }
    else
        cout << "It remains decolete.\n";
}
void Planet::Print() {
    cout << "This is " << name << endl << ". It has a total of " << moons << " moon(s), " << rings << " ring(s) and is ";
    if (!life)
        cout << "not ";
    cout << "habiting life.\n I am a";
    switch (type) {
    case 'a':
        cout << "n Astral Anomaly";
        break;
    case 'b':
        cout << " Brown Dwarf";
        break;
    case 'c':
        cout << " Collision instance";
        break;
    case 'd':
        cout << " Black Hole";
        break;
    case 'e':
        cout << " White Dwarf";
        break;
    case 'f':
        cout << " Red Giant";
        break;
    case 'g':
        cout << " Gas Giant";
        break;
    case 'h':
        cout << " Great Attractor";
        break;
    case 'i':
        cout << " Ice World";
        break;
    case 'j':
        cout << " Runaway Greenhouse World";
        break;
    case 'k':
        cout << " Cluster";
        break;
    case 'l':
        cout << " Red Dwarf";
        break;
    case 'm':
        cout << " Space Ship";
        break;
    case 'n':
        cout << " Neutron Star";
        break;
    case 'o':
        cout << "n Orbit";
        break;
    case 'p':
        cout << " Perfect Planet";
        break;
    case 'q':
        cout << " Red Dwarf";
        break;
    case 'r':
        cout << " Rocky Planet";
        break;
    case 's':
        cout << " Main Sequence Star";
        break;
    case 't':
        cout << " Tidally Locked Object";
        break;
    case 'u':
        cout << " Universal Constant";
        break;
    case 'v':
        cout << " Virtual Planet";
        break;
    case 'w':
        cout << " Water World";
        break;
    case 'x':
        cout << " Unidentified Planet";
        break;
    case 'y':
        cout << " Yellow Dwarf";
        break;
    case 'z':
        cout << " Dwarf Planet";
        break;
    default:
        cout << " Unknown Object";
        break;
    }
    cout << ".\n";
}