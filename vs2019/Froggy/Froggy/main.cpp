#include "frog.h"
#include "car.h"
#include"globals.h"
#include<SFML/Graphics.hpp>
#include<iostream>
using namespace sf;

bool coolaid(frog play, car thing);
bool cooler(frog play, vector<car*>::iterator thang);

int main() {
	//game variables and setup
	srand(time(NULL));
	bool aqua = false;
	bool keys[] = { false, false, false, false };
	bool isdie = false;
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
	vector<car*> logs;
	for (int i = 0; i<5;i++)
		for (int j = 0; j < 2; j++) {
			cars.push_back(new car(i * 400 + 100, j * 200 + 500, LEFT));
			cars.push_back(new car(i * 300 + 200, j * 200 + 600, RIGHT));
		}

	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 2; j++) {
			logs.push_back(new car(i * 400 + 100, j * 200 + 50, LEFT, .03f, true));
			logs.push_back(new car(i * 300 + 200, j * 200 + 150, RIGHT, .03f, true));
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
		for (vector<car*>::iterator i = cars.begin(); i != cars.end(); i++) {
			(*i)->move();
		}
		for (vector<car*>::iterator i = logs.begin(); i != logs.end(); i++) {
			(*i)->move();
		}

		//VIBE CHECKING!!!
		if (player.returnY() < 380 )
			aqua = true;
		else
			aqua = false;
		for (vector<car*>::iterator i = logs.begin(); i != logs.end(); i++) {
			if (aqua && !cooler(player, i)) { //Death to the player if he dares to enter the water without a log
				isdie = true;
			}
		}
		for (vector<car*>::iterator i = cars.begin(); i != cars.end(); i++) {
			if (cooler(player,i))
				isdie = true;
		}

		//MAKE THINGS APPEAR FOR YOUR PHOTO RECEPTORS (aka render)
		screen.draw(WaterWay);
		

		
		for (vector<car*>::iterator i = logs.begin(); i != logs.end(); i++) {
			(*i)->draw(screen);
		}
		player.draw(screen);
		for (vector<car*>::iterator i = cars.begin(); i != cars.end(); i++) {
			(*i)->draw(screen);
		}



		screen.display();
		screen.clear();

		//EXECUTE THE PLAYER
		if (isdie) {
			isdie = false;
			player.ded();
		}


	}//END GAME LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-
	std::cout << "Gaem Ovrre.\n";
	return 0;
}

bool coolaid(frog play, car thing) {
	return (thing.collide(play.returnX(), play.returnY()) || thing.collide(play.returnX() + 20, play.returnY()) || thing.collide(play.returnX(), play.returnY() + 20) || thing.collide(play.returnX() + 20, play.returnY() + 20));
}
bool cooler(frog play, vector<car*>::iterator thang) {
	return ((*thang)->collide(play.returnX(), play.returnY()) || (*thang)->collide(play.returnX() + 20, play.returnY()) || (*thang)->collide(play.returnX(), play.returnY() + 20) || (*thang)->collide(play.returnX() + 20, play.returnY() + 20));
}