#include "ball.h"
ball::ball(float x, float y) {
	xpos = x;
	ypos = y;
	bvx = true;
	bvy = true;
}

void ball::draw(sf::RenderWindow& window) {
	circ.setRadius(25);
	circ.setFillColor((sf::Color(0, 200, 0)));
	circ.setPosition(xpos, ypos);
	window.draw(circ);
}
float ball::bx() { return xpos; }
float ball::by() { return ypos; }
void flipx(bool dir) {
	bvx = dir;
}
void flipx(bool dir) {
	bvy = dir;
}
void ball::step() {
	if (bvx)
		xpos += 0.1f;
	else
		xpos -= 0.1f;
	if (bvy)
		ypos += 0.1f;
	else
		ypos -= 0.1f;
}

void ball::setpos(float x, float y) {
	xpos = x;
	ypos = y;
}