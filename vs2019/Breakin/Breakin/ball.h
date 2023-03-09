#pragma once
#include <SFML/Graphics.hpp>

class ball
{
private:
	float xpos;
	float ypos;
	bool bvx;
	bool bvy;
	sf::CircleShape circ;
public:
	ball(float x, float y); //constructor
	void draw(sf::RenderWindow& window);
	void step();
	float bx();
	float by();
	void setpos(float x, float y);
	void flipx(bool dir);
	void flipy(bool dir);
};

