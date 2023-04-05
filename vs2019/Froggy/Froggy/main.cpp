#include "frog.h"
#include "car.h"
#include"globals.h"
#include<SFML/Graphics.hpp>
#include<iostream>
using namespace sf;

bool coolaid(frog play, car thing);

int main() {
	//game variables and setup
	srand(time(NULL));
	bool aqua = false;
	bool keys[] = { false, false, false, false };
	int timer = 0;
	//SFML boilerplate stuff
	RenderWindow screen(VideoMode(1000, 1000), "Froggers.");
	frog player;
	car light(500,500,LEFT);
	car frend(200, 340, RIGHT, .03f, true);
	car jerry(450, 450, RIGHT);
	car harry(100, 200, RIGHT, .03f, true);
	car berry(500, 100, LEFT, .03f, true);
	vector<car*> cars;
	for (int i = 0; i<5;i++)
		for (int j = 0; j < 1; j++) {
			cars.push_back(new car(i * 400 + 100, j * 200 + 500, LEFT));
			cars.push_back(new car(i * 300 + 200, j * 200 + 600, RIGHT));
		}
	RectangleShape WaterWay(Vector2f(1000, 400));
	WaterWay.setFillColor(Color(10, 0, 255));
	WaterWay.setPosition(0, 0);
	
	while (screen.isOpen()) {//GAME L0OP, GAME OPAPA, 1 ! GAME LOOOOOOOOOOOOOOOOOOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		//INPOOP, Input Input not output INPUT!
		Event event;
		while (screen.pollEvent(event)) {
			if (event.type == Event::Closed)
				screen.close();
			if (Keyboard::isKeyPressed(Keyboard::Up))
				keys[UP] = true;
			else
				keys[UP] = false;
			if (Keyboard::isKeyPressed(Keyboard::Down))
				keys[DOWN] = true;
			else
				keys[DOWN] = false;
			if (Keyboard::isKeyPressed(Keyboard::Left))
				keys[LEFT] = true;
			else
				keys[LEFT] = false;
			if (Keyboard::isKeyPressed(Keyboard::Right))
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
		frend.move();
		berry.move();
		jerry.move();
		harry.move();


		//VIBE CHECKING!!!
		if (player.returnY() < 380 )
			aqua = true;
		else
			aqua = false;
		if (aqua && !coolaid(player, frend) && !coolaid(player, harry) && !coolaid(player, berry)) { //Death to the player if he dares to enter the water without a log
			screen.draw(WaterWay);
			light.draw(screen);
			frend.draw(screen);
			player.draw(screen);
			screen.display();
			screen.clear();
			player.ded();
		}
		if (coolaid(player, frend)) {
			player.flaplex(frend.givsped());
		} else if (coolaid(player, harry)) {
			player.flaplex(frend.givsped());
		} else if (coolaid(player, berry)) {
			player.flaplex(frend.givsped());
		}
		if (coolaid(player, light)){
			screen.draw(WaterWay);
			light.draw(screen);
			frend.draw(screen);
			player.draw(screen);
			screen.display();
			screen.clear();
			player.ded();
		} else if (coolaid(player, jerry)) {
			screen.draw(WaterWay);
			light.draw(screen);
			frend.draw(screen);
			player.draw(screen);
			screen.display();
			screen.clear();
			player.ded();
		}
		//MAKE THINGS APPEAR FOR YOUR PHOTO RECEPTORS (aka render)
		screen.draw(WaterWay);
		light.draw(screen);
		frend.draw(screen);
		jerry.draw(screen);
		harry.draw(screen);
		berry.draw(screen);
		player.draw(screen);
		screen.display();
		screen.clear();
		

	}//END GAME LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-
	std::cout << "Gaem Ovrre.\n";
	return 0;
}

bool coolaid(frog play, car thing) {
	return (thing.collide(play.returnX(), play.returnY()) || thing.collide(play.returnX() + 20, play.returnY()) || thing.collide(play.returnX(), play.returnY() + 20) || thing.collide(play.returnX() + 20, play.returnY() + 20));
}