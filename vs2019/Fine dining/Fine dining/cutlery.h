#pragma once
#include <iostream>
using namespace std;
class cutlery
{
private:
	int type;
	bool isClean;
public:
	cutlery(int ty);
	void printInfo();
	void use() { isClean = false; }
	void wash() { isClean = true; }
};

