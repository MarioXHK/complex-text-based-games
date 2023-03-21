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
	pack = false;
	fire = 300;
	dis = 20;
	speed = 200;
}

void frog::draw(RenderWindow& window) {
	RectangleShape FrogPic(Vector2f(20, 20));
	FrogPic.setFillColor(Color(50, 200, 50));
	FrogPic.setPosition(xpos, ypos);
	window.draw(FrogPic);
}

void frog::jump(bool* keys) {
	if (pack)
		return;
	if (keys[UP])
		yVel = 0-dis;
	else if (keys[DOWN])
		yVel = dis;
	else
		yVel = 0;
	if (keys[LEFT])
		xVel = 0-dis;
	else if (keys[RIGHT])
		xVel = dis;
	else
		xVel = 0;
	xpos += xVel;
	ypos += yVel;
}
void frog::pac(bool* keys) {
	if (fire > speed) {
		if (pack)
			return;
		if (keys[UP])
			yVel = 0-dis;
		else if (keys[DOWN])
			yVel = dis;
		else
			yVel = 0;
		if (keys[LEFT])
			xVel = 0-dis;
		else if (keys[RIGHT])
			xVel = dis;
		else
			xVel = 0;
		if (keys[LEFT] || keys[UP] || keys[DOWN] || keys[RIGHT]) {
			fire = 0;
			pack = true;
		}
	}
}
void frog::pacupdate() {
	fire++;
	if (pack) {
		xpos += xVel/ speed;
		ypos += yVel/speed;
		if (fire > speed)
			pack = false;
	}
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