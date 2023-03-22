#include "cutlery.h"
#include <iostream>
using namespace std;

cutlery::cutlery(int ty) {
	type = ty;
	isClean = true;
}
void cutlery::printInfo() {
	cout << "This is a ";
	if (type == 0)
		cout << "fork ";
	else if (type == 1)
		cout << "spoon ";
	else if (type == 2)
		cout << "knife ";
	else
		cout << "silver ingot ";
	cout << "that is ";
	if (!isClean)
		cout << "un";
	cout << "clean.\n";
}