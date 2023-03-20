#pragma once
#include<SFML/Graphics.hpp>

//class definition for birb
class flower {

private: //private stuff can only be seen/used by fellow class members

	//usually you keep variables private and functions public, but they can definitely not be that way too.
	int xpos;
	int ypos;
	int color[3]; //3-slot array to hold the birb's color. Remember, C++ arrays are a lot like python lists.
	int colour[3];
	int ogx;
	int ogy;

	sf::CircleShape body;
	sf::CircleShape peddle; //SFML lets you set the number of sides of a circle, so this is how we make a triangle!
	sf::RectangleShape stem;

public: //public stuff can be seen/used by errbody in the clurb

	//you *can* have the whole definitions here, but its best to have just the declarations unless they are super short
	flower(int x, int y, int c[3], int e[3]); //parameterized constructor
	int getx();
	int gety();
	void changeColor(int c[3], int e[3]);
	void draw(sf::RenderWindow& window);

};
