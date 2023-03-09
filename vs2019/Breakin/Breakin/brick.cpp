#include"brick.h"
brick::brick(int x, int y) {
	xpos = x;
	ypos = y;

}

void brick::draw(sf::RenderWindow& window) {
	rect.setSize(sf::Vector2f(100, 50));
	rect.setFillColor((sf::Color(0, 200, 0)));
	rect.setPosition(xpos, ypos);
	window.draw(rect);
}