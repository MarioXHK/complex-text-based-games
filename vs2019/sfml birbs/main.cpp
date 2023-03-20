#include<SFML/Graphics.hpp>
#include "birb.h"
#include "flower.h"
int main() {

	//this next line is an array. Arrays are a lot like python lists.
	int birbColor[] = { 255, 200, 200 }; //set up an array of colors to make your birb PINK!
	int queenColor[] = { 255, 50, 200 };
	int steveColor[] = { 20,60,250 };
	int greeColor[] = { 10,255,60 };
	int cool[] = { 200, 150, 0 };
	int WHITE[] = {255, 255, 255};
	int YELLOW[] = { 255, 255, 0 };
	int rainred = 255;
	int raingreen = 0;
	int rainblue = 0;
	int boss = 25;
	bool incred = false;
	bool incgreen = false;
	bool incblue = false;
	bool decred = false;
	bool decgreen = false;
	bool decblue = false;
	bool giraffe = true;
	//instantiate birbs
	int badTimer = 0;
	birb Steve(100, 100, steveColor);
	birb Alex(200, 200, birbColor);
	birb Tommy(300, 300, birbColor);
	birb Sans(400, 400, WHITE);
	birb Xander(500, 500, birbColor);
	birb Nyan(600, 600, WHITE);
	birb Queen(700, 400, queenColor);
	flower majesty(400, 600, YELLOW, WHITE);
	sf::RenderWindow window(sf::VideoMode(800, 800), "Happy Spring!"); //set up game window


	while (1) {//GAME LOOP OMG
		//Decided to port my old paint rainbow code here for no reason!!!
		if (rainred == 255 && raingreen == 0 && rainblue == 0) {
			decblue = false;
			incgreen = true;
		}
		else if (rainred == 255 && raingreen == 255 && rainblue == 0) {
			decred = true;
			incgreen = false;
		}
		else if (rainred == 0 && raingreen == 255 && rainblue == 0) {
			decred = false;
			incblue = true;
		}
		else if (rainred == 0 && raingreen == 255 && rainblue == 255) {
			decgreen = true;
			incblue = false;
		}
		else if (rainred == 0 && raingreen == 0 && rainblue == 255) {
			decgreen = false;
			incred = true;
		}
		else if (rainred == 255 && raingreen == 0 && rainblue == 255) {
			incred = false;
			decblue = true;
		}
		if (incred)
			rainred++;
		if (incgreen)
			raingreen++;
		if (incblue)
			rainblue++;
		if (decred)
			rainred--;
		if (decgreen)
			raingreen--;
		if (decblue)
			rainblue--;
		//flapping section!!!!!!!!!!!!!!!!
		if (rand() % 100 < 3)
			Steve.flap();
		if (rand() % 100 < 3)
			Alex.flap();
		if (rand() % 100 < 3)
			Alex.flap();
		if (rand() % 100 < 3)
			Tommy.flap();
		if (rand() % 100 == 0)
			Sans.flap();
		if (rand() % 100 < 3)
			Xander.flap();
		if (rand() % 100 < 3)
			Nyan.flap(-1);
		if (rand() % 100 < 3) {
			if (Queen.gety() < 400)
				boss--;
			else if (Queen.gety() > 400)
				boss++;
			Queen.flap(boss);
		}
		//Color change section----------------------------------------------
		int rainBow[] = { rainred,raingreen,rainblue };
		int random[] = {rand() % 256,rand() % 256 ,rand() % 256 };
		Tommy.cchange(rainBow);
		Xander.cchange(random);
		//RENDER SECTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		Steve.draw(window);
		Alex.draw(window);
		Tommy.draw(window);
		Sans.draw(window);
		Xander.draw(window);
		Nyan.draw(window);
		Queen.draw(window);
		majesty.draw(window);
		window.display();
		if (giraffe)
			window.clear();
	}
}


