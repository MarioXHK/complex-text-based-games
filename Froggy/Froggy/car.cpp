#include "car.h"
#include "globals.h"
#include<SFML/Graphics.hpp>
//constructor
car::car(float x, float y, int dir, float sped, bool cool) {
	xpos = x;
	ypos = y;
	speed = sped;
	direction = dir;
	if (cool) {
		red = rand() % 150 + 101;
		green = red-(60+(rand() % 41));
		blue = 0;
	}
	else {
		red = 250;
		green = rand() % 100 + 101;
		blue = rand() % 100 + 101;
	}
}

void car::draw(sf::RenderWindow& window) {
	sf::RectangleShape vehicle(sf::Vector2f(100, 50));
	vehicle.setFillColor(sf::Color(red, green, blue));
	vehicle.setPosition(xpos, ypos);
	window.draw(vehicle);
}
void car::move() {
	if (direction == LEFT) {
		if (xpos < -100)
			xpos = 1100;
		xpos -= speed;
	}
	else if (direction == RIGHT) {
		if (xpos > 1100)
			xpos = -100;
		xpos += speed;
	}
}

bool car::collide(int x, int y) {
	if ((x >= xpos && xpos + 100 >= x) && (y >= ypos && ypos + 50 >= y))
		return true;
	else
		return false;
}