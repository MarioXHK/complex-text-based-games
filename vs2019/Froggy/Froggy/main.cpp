#include "frog.h"
#include"globals.h"
#include<SFML/Graphics.hpp>
#include<iostream>

int main() {
	//game variables and setup
	srand(time(NULL));
	bool keys[] = { false, false, false, false };

	//SFML boilerplate stuff
	sf::RenderWindow screen(sf::VideoMode(1000, 1000), "Froggers.");

	while (screen.isOpen()) {//GAME L0OP, GAME OPAPA, 1 ! GAME LOOOOOOOOOOOOOOOOOOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		//INPOOP, Input Input not output INPUT!
		sf::Event event;
		while (screen.pollEvent(event)) {
			if (event.type == sf::Event::Closed)
				screen.close();
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
				keys[UP] = true;
			}
			else
				keys[UP] = false;
		}
		//THe laws of physics (physics section)

		//MAKE THINGS APPEAR FOR YOUR PHOTO RECEPTORS (aka render)
	}//END GAME LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-
	std::cout << "Gaem Ovrre.\n";
	return 0;
}