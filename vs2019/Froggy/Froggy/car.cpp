#include "car.h"
#include "globals.h"
#include<SFML/Graphics.hpp>
//constructor
car::car(float x, float y, int dir) {
	xpos = x;
	ypos = y;
	direction = dir;
	green = rand() % 100 + 101;
	blue = rand() % 100 + 101;
}

void car::draw(sf::RenderWindow& window) {
	sf::RectangleShape vehicle(sf::Vector2f(100, 50));
	vehicle.setFillColor(sf::Color(250, green, blue));
	vehicle.setPosition(xpos, ypos);
	window.draw(vehicle);
}
void car::move() {
	if (direction == LEFT) {
		if (xpos < -100)
			xpos = 1100;
		xpos -= .1;
	}
}

bool car::collide(int x, int y) {
	if ((x >= xpos && xpos + 100 >= x) && (y >= ypos && ypos + 50 >= y))
		return true;
	else
		return false;
}