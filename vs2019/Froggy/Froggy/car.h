#pragma once
#include<SFML/Graphics.hpp>
#include<iostream>
#include "globals.h"
class car
{
private:
	float xpos;
	float ypos;
	float speed;
	int red;
	int green;
	int blue;
	bool cool;
	int direction;
public:
	car(float x, float y, int dir = RIGHT, float sped = .1f, bool cool = false);
	void draw(sf::RenderWindow& window);
	void move();
	bool collide(int x, int y);
	void printInfo() { std::cout << "I AM A BOX AND MY POSITION IS " << xpos << ", " << ypos << "\n"; }
	float givsped() { return speed; }
};

