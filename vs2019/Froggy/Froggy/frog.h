#pragma once
#include<SFML/Graphics.hpp>
#include<iostream>
using namespace std;

class frog
{
private:
	float xpos;
	float ypos;
	int lives;
	float xVel;
	float yVel;
public:
	frog();
	void draw(sf::RenderWindow &window);
	void jump(bool *keys);
	float returnX() { return xpos; }
	float returnY() { return ypos; }
	void ded();
	int returnLives() { return lives; }
	void printInfo() { cout << "I am a frog any my position is " << xpos << ", " << ypos << endl; }
};

