#include "frog.h"
#include "car.h"
#include"globals.h"
#include<SFML/Graphics.hpp>
#include<iostream>

int main() {
	//game variables and setup
	srand(time(NULL));
	bool keys[] = { false, false, false, false };
	int timer = 0;
	//SFML boilerplate stuff
	sf::RenderWindow screen(sf::VideoMode(1000, 1000), "Froggers.");
	frog player;
	car light(500,500,LEFT);

	vector<car*> cars;
	for (int i = 0; i<5;i++)
		for (int j = 0; j < 1; j++) {
			cars.push_back(new car(i * 400 + 100, j * 200 + 500, LEFT));
			cars.push_back(new car(i * 300 + 200, j * 200 + 600, RIGHT));
		}

	while (screen.isOpen()) {//GAME L0OP, GAME OPAPA, 1 ! GAME LOOOOOOOOOOOOOOOOOOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		//INPOOP, Input Input not output INPUT!
		sf::Event event;
		while (screen.pollEvent(event)) {
			if (event.type == sf::Event::Closed)
				screen.close();
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
				keys[UP] = true;
			else
				keys[UP] = false;
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
				keys[DOWN] = true;
			else
				keys[DOWN] = false;
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
				keys[LEFT] = true;
			else
				keys[LEFT] = false;
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
				keys[RIGHT] = true;
			else
				keys[RIGHT] = false;
			
		}
		//THe laws of physics (physics section)
		timer++;
		if (timer > 500 && (keys[LEFT]|| keys[UP]|| keys[DOWN]||keys[RIGHT])) {
			player.pac(keys);
			timer = 0;
		}
		player.pacupdate();
		light.move();
		if (light.collide(player.returnX(), player.returnY()) || light.collide(player.returnX()+20, player.returnY()) || light.collide(player.returnX(), player.returnY() + 20) || light.collide(player.returnX() + 20, player.returnY() + 20)){
			player.draw(screen);
			light.draw(screen);
			screen.display();
			screen.clear();
			player.ded();
		}
		//MAKE THINGS APPEAR FOR YOUR PHOTO RECEPTORS (aka render)
		player.draw(screen);
		light.draw(screen);
		screen.display();
		screen.clear();
		

	}//END GAME LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-
	std::cout << "Gaem Ovrre.\n";
	return 0;
}