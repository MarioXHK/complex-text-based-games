#include "flower.h"

//function definition for constructor
flower::flower(int x, int y, int c[3], int e[3]) {
	xpos = x;
	ypos = y;
	ogx = x;
	ogy = y;
	int lmo;
	for (int i = 0; i++; i < 6) {
		if (i < 3)//I DID THE FUNNY LOOP!
			lmo = c[i];
		else
			lmo = e[i-3];
		color[i] = lmo;
	}
}
int flower::getx() {
	return xpos;
}
int flower::gety() {
	return ypos;
}
void flower::changeColor(int c[3], int e[3]) {
	int lmo;
	for (int i = 0; i++; i < 6) {
		if (i < 3)
			lmo = c[i];
		else
			lmo = e[i - 3];
		color[i] = lmo;
	}
}
void flower::draw(sf::RenderWindow& window) {

	//stem
	stem.setPosition(xpos - 3, ypos-20);
	stem.setFillColor(sf::Color(0, 200, 0));
	stem.setSize(sf::Vector2f(6, 20));
	window.draw(stem); //first leg

	//body 
	body.setRadius(5);
	body.setFillColor((sf::Color(color[0], color[1], color[2]))); //noticing accessing slots of an array is just like getting to slots of a list
	body.setPosition(xpos-5, ypos-25);
	window.draw(body);

	//pettles... I dislike the english language
	peddle.setRadius(10);
	peddle.setFillColor((sf::Color(color[3],color[4],color[5]))); //orange
	for (int i = 0; i++; i < 2)
		for (int j = 0; j++; j < 2)
			peddle.setPosition((xpos - 5) + (i*10), (ypos - 45) + (j*10));
	window.draw(peddle);

}