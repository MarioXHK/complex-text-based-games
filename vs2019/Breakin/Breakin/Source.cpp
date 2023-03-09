#include <SFML/Graphics.hpp>
#include"brick.h"
#include"ball.h"

//instantiate some bricks
brick b1(0, 0);
brick b2(100, 0);
brick b3(200, 0);
brick b4(300, 0);
brick b5(400, 0);
brick b6(500, 0);
brick b7(600, 0);
brick b8(700, 0);
brick b9(0, 100);
brick b10(100, 100);
brick b11(200, 100);
brick b12(300, 100);
brick b13(400, 100);
brick b14(500, 100);
brick b15(600, 100);
brick b16(700, 100);
ball b0(400, 400);

int main()
{
	sf::RenderWindow window(sf::VideoMode(800, 800), "Breakout"); //set up screen
	sf::RectangleShape rect;
	sf::CircleShape circ;
	float ballx = 400.0f;
	float bally = 400.0f;
	if (1.0f == 1)
		bool hi = true;
	while (window.isOpen())//GAME LOOP--------------------------------
	{
		//input section--------------------------------
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();

		}
		//physics section------------------------------
		b0.step();

		//render section-------------------------------
		window.clear();

		//draw bricks
		b0.draw(window);
		b1.draw(window);
		b2.draw(window);
		b3.draw(window);
		b4.draw(window);
		b5.draw(window);
		b6.draw(window);
		b7.draw(window);
		b8.draw(window);
		b9.draw(window);
		b10.draw(window);
		b11.draw(window);
		b12.draw(window);
		b13.draw(window);
		b14.draw(window);
		b15.draw(window);
		b16.draw(window);
		window.display(); //flip the buffer

	}//end game loop-------------------------------------------------

	return 0;
} //end main