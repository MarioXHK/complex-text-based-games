
#include <iostream>
using namespace std;
int main()
{
    cout << "I don't actually know what these things are.\nAlso endl is a lie I can just use the same thing I did in python." << endl << "Although endl is more readable.";
    cout << endl << "So.... Song choice!" << endl;
    cout << "1: all star, 2: basics in behavior, 3: that's what I do, 4: nyan cat, 5: sad,\n6: mystery song! Or 7: quit\n";
    int choice;
    cin >> choice;
    switch (choice) {
    case 1:
        cout << "Hey now, you're an all-star, get your game on, go play" << endl << "Hey now, you're a rock star, get the show on, get paid" << endl << "And all that glitters is gold" << endl << "Only shooting stars break the mold" << endl;
    break;
    case 2:
        cout << "This is how we live our lives searchin'\nFor the answers inside of every page\nAnd I'm here wonderin' if one day\nWe'll finally be free from this cage\nIs it okay to have a feelin'\nThat maybe there is more to this game?\nHowever now, no time to question\nSo just behave" << endl;
        break;
    case 3:
        cout << "Get your PRIZE!" << endl;
        cout << "Won't you come on IN?" << endl;
        cout << "Into my SCHOOLHOUSE!?" << endl;
        cout << "Stay the course and follow through," << endl;
        cout << "I'm slowly coming after you!" << endl;
        cout << "I'll bring the PUNISHMENT" << endl;
        cout << "THAT'S WHAT I DO" << endl;
        cout << "you know it's tru!E :)" << endl;
        break;
    case 4:
        for (int i = 0; i < 64; i++)
            cout << "nyan" << endl;
        break;
    case 5:
        cout << "Seasonal Affective Disorder\nEverything can stop on a quarter" << "Got no prospects" << "(Cold plus hopeless : Cope less)" << endl << "It's the snow's\nfault Got no girlfriend" << "(Cold plus listless : Kissed less)\nPass the snow salt" << endl;
        break;
    case 6:
        cout << "We're no strangers to love You know the rules and so do I (do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (to say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you" << endl;
        break;
    case 7:
        cout << endl;
        break;
    default:
        cout << "That is not an option." << endl;
    }
}