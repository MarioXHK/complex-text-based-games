// Things.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int MonsterGen(int life, char biome);


int main()
{
    int health = 30;
    cout << "Hello World!\n";
    health = MonsterGen(health, 'p');
    if (health <= 0) {
        cout << "You ran out of health and were knocked down...\nThe end.\n";
        return 0;
    }
}


int MonsterGen(int life, char biome) {
    int num = rand() % 100;
    cout << num << endl;
    string monster = "nul";
    if (biome == 'p') {
        if (num < 20) {
            monster = "spider";
        }
        else if (num < 50)
            monster = "zombie";
        else if (num < 75)
            monster = "skeleton";
        else if (num < 80)
            monster = "witch";
    }
    int monhealth = 10;
    int monatkmod = 10;
    if (monster == "spider") {
        monhealth = 3;
        monatkmod = 1;
        cout << "A spider that's as small as your thumb appears.\nDespite it's size, you fear it with all your heart even though the spider fears you more than you fear it.\nIt is simply about to choose self defence to save it's own life.\n";
    }
    else if (monster == "zombie") {
        monhealth = 15;
        monatkmod = 4;
        cout << "The cold rotting corpse of a past traveler begins moving once again.\nThe lifeless body fighting back from the inevitability of death itself, willingly or not.\nThe zombie is livid at you, and all your living.\nWhile it would wish for this suffering to not happen to another soul, it's body rushes towards you in a rage to make it so.\n";
    }
    else if (monster == "skeleton"){
        monhealth = 12;
        monatkmod = 5;
        cout << "A skeleton wanders around aimlessly.\nIt has been traveling for a long time, all to find a new body, as for it's own has long since seaced breathing.\nIt then finally finds you. It has no other choice now, as it is likely to not find another person around.\nYou know only one of you are getting out of this.\n";
    }
    else if (monster == "witch"){
        monhealth = 20;
        monatkmod = 5;
        cout << "The curious witch stumbles through the surrounding area, wandering and looking for... something.\nOnce you're up to it, it looks at you with odd intent.\nYou're unsure what it's intentions could be, but judging by the witch's look and aura, it's likely not good.\n";
    }
    else if (monster == "nul") {
        cout << "The wind breezes about as it appears that nobody has came.\nThe silence is near overwhelming, but safe.\n";
        return life;
    }else {
        cout << "You're not sure what you've encountered, but you run away before you could interact with it.\n";
        return life;
    }
    char opt = '0';
    int atg;
    while (monhealth > 0 && life > 0) {
        cout << "your health is " << life << ". You can (a)ttack, (h)eal, or (f)lee.\n";
        cin >> opt;
        while (!(opt == 'a' || opt == 'h' || opt == 'f'))
            cin >> opt;
        atg = rand() % 5 + 4;
        if (opt == 'a') {
            cout << "you attack and deal " << atg << " damage!\n";
            monhealth -= atg;
        }
        else if (opt == 'h') {
            life += atg;
            if (life > 30){
                life = 30;
                cout << "Your health is maxed out!\n";
            }
            else {
                cout << "You heal " << atg << "health!\n";
            }
        }
        else {
            cout << "You flee the battle!\n";
            return life;
        }
        if (monhealth > 0) {
            atg = rand() % 5 + monatkmod;
            cout << "The " << monster << " attacks and deals " << atg << " damage!\n";
        }
    }
    if (monhealth <= 0) {
        cout << "The " << monster << " was defeated!\n";
    }
    return life;
}