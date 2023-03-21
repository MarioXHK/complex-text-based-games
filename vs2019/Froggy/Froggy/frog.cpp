#include "frog.h"
#include"globals.h"
#include<SFML/Graphics.hpp>
#include<Windows.h>
using namespace sf;

//constructor
frog::frog() {
	xpos = 500;
	ypos = 954;
	lives = 5;
	xVel = 0;
	yVel = 0;
}

void frog::draw(RenderWindow& window) {
	RectangleShape FrogPic(Vector2f(20, 20));
	FrogPic.setFillColor(Color(50, 200, 50));
	FrogPic.setPosition(xpos, ypos);
	window.draw(FrogPic);
}

void frog::jump(bool* keys) {
	if (keys[UP])
		yVel = -50;
	else if (keys[DOWN])
		yVel = 50;
	else
		yVel = 0;
	if (keys[LEFT])
		xVel = -50;
	else if (keys[RIGHT])
		xVel = 50;
	else
		xVel = 0;
	xpos += xVel;
	ypos += yVel;
}
//MURDER:bangbang:
void frog::ded() {
	//play explosion sound here
	std::cout << "AAAA DEATH!!!\n";
	Beep(500, 500);
	lives--;
	xpos = 500;
	ypos = 954;
}