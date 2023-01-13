#include <iostream>
using namespace std;

int main() {
	for (int a = 50; a <= 70; a += 2)
		cout << a << " ";
	cout << endl;
	for (int b = 100; b >= 50; b -= 5)
		cout << b << " ";
	cout << endl;
	for (int c = 2; c <= 2048; c *= 2)
		cout << c << " ";
	cout << endl;
	for (int d = 0; d < 10; d++) {
		for (int e = 0; e < 6; e++)
			cout << "*";
		cout << endl;
	}
	for (int f = 0; f < 4; f++) {
		for (int g = 1; g <= 4; g++)
			cout << g << " ";
		cout << endl;
	}
	cout << "Can I go home yet?" << endl;
}