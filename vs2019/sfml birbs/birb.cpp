#include"birb.h"

//function definition for constructor
birb::birb(int x, int y, int c[3]) {
	xpos = x;
	ypos = y;
	ogx = x;
	ogy = y;
	color[0] = c[0]; //if our array was any longer I would have used a for loop here :)
	color[1] = c[1];
	color[2] = c[2];

}
int birb::getx() {
	return xpos;
}
int birb::gety() {
	return ypos;
}
void birb::cchange(int c[3]) {
	color[0] = c[0];
	color[1] = c[1];
	color[2] = c[2];
}
//function definition for draw
void birb::flap(int p) {
	ypos-=p;
}
void birb::draw(sf::RenderWindow& window) {

	//leggies
	feets.setPosition(xpos + 10, ypos + 35);
	feets.setFillColor(sf::Color(200, 150, 0));
	feets.setSize(sf::Vector2f(5, 15));
	window.draw(feets); //first leg
	feets.setPosition(xpos + 25, ypos + 35);
	window.draw(feets); //second leg

	//body 
	body.setRadius(20);
	body.setFillColor((sf::Color(color[0], color[1], color[2]))); //noticing accessing slots of an array is just like getting to slots of a list
	body.setPosition(xpos, ypos);
	window.draw(body);
	
	//birb eyes
	body.setRadius(4);
	body.setFillColor((sf::Color(0,0,0))); //black
	body.setPosition(xpos+15, ypos+10);
	window.draw(body); //first eye
	body.setPosition(xpos + 30, ypos + 10);
	window.draw(body); //second eye

	//birb beak
	beak.setPointCount(3); //make it a triangle
	beak.setRadius(10);
	beak.setFillColor((sf::Color(200, 150, 0))); //orange
	beak.setPosition(xpos + 17, ypos + 10);
	window.draw(beak);

}