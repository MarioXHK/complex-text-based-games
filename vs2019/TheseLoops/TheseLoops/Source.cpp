#include <iostream>
using namespace std;

void Snowflake(int stuff);

int main() {
    cout << "Hello, Loops!" << endl;
    for (int i = 0; i < 10; i++)
        cout << i << " ";
    cout << endl;
    for (int j = 5; j <= 30; j += 5)
        cout << j << " ";
    cout << endl;
    for (int k = 100; k >= 0; k -= 10)
        cout << k << " ";
    cout << endl;
    for (int l = 2; l < 40; l *= 2)
        cout << l << " ";
    cout << endl;
    for (int m = 70; m <= 80; m++)
        cout << m << " ";
    cout << endl;
    for (int n = 100; n <= 300; n += 20)
        cout << n << " ";
    cout << endl;
    for (int o = 25; o >= -25; o -= 5)
        cout << o << " ";
    cout << endl;
    for (int p = 10000; p >= 10; p /= 5)
        cout << p << " ";
    cout << endl;
    
    for (int q = 0; q < 10; q++) {//Creates snowflakes of ever increasing sizes
        cout << endl;
        Snowflake(q);
        cout << endl;
    }
    cout << "Goodbye, Loops!" << endl;
}
//The function of how to do snowflakes!
void Snowflake(int stuff) {
    int eb = stuff * 2;
    for (int h = eb; h >= 0; h -= 2) {
        for (int j = h/2; j < eb-1; j++)
            cout << " ";//the spaces in front
        cout << "_\\/";
        for (int i = 0; i < h; i++)
            cout << " ";//the spaces in the middle
        cout << "\\/_" << endl;
    }//The upper snowflake
    for (int i = 0; i <= stuff; i++)
        cout << "_\\";
    for (int i = 0; i <= stuff; i++)
        cout << "/_";
    cout << endl;//THE MIDDLE
    for (int i = 0; i <= stuff; i++)
        cout << " /";
    for (int i = 0; i <= stuff; i++)
        cout << "\\ ";
    cout << endl;
    for (int k = 0; k <= eb; k += 2) {
        for (int j = k / 2; j < eb - 1; j++)
            cout << " ";
        cout << "_/\\";
        for (int i = 0; i < k; i++)
            cout << " ";
        cout << "/\\_" << endl;
    }//the lower snowflake
}