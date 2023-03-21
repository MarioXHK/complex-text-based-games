#pragma once
#include<SFML/Graphics.hpp>
#include<iostream>
class car
{
private:
	float xpos;
	float ypos;
	int green;
	int blue;
	int direction;
public:
	car(float x, float y, int dir);
	void draw(sf::RenderWindow& window);
	void move();
	bool collide(int x, int y);
	void printInfo() { std::cout << "I AM A CAR AND MY POSITION IS " << xpos << ", " << ypos << "\n"; }
};

