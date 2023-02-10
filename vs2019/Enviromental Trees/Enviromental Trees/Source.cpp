#include <SFML/Graphics.hpp> //bring in library


int main() //starting point of all C++ programs
{
	sf::RenderWindow window(sf::VideoMode(800, 800), "Trees"); //set up screen
	sf::CircleShape circle; //tell the program we're using this shape
	sf::RectangleShape rect; //this one too!



	while (window.isOpen())//GAME LOOP--------------------------------
	{
		sf::Event event; //look for keyboard/mouse/etc clicks
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed) //check if player has closed window with top left 'x' button
				window.close();

		}

		//render section-------------------------------
		window.clear(); //wipe screen (needed more for animations)

		//left branch
		circle.setRadius(30);
		circle.setFillColor((sf::Color(0, 100, 80)));
		circle.setPosition(200, 180);
		window.draw(circle);

		//right branch
		circle.setRadius(30);
		circle.setFillColor((sf::Color(80, 100, 0)));
		circle.setPosition(250, 180);
		window.draw(circle);

		//top branch
		circle.setRadius(30);
		circle.setFillColor((sf::Color(0, 100, 0)));
		circle.setPosition(225, 150);
		window.draw(circle);

		//trunk
		rect.setPosition(245, 200);
		rect.setFillColor(sf::Color(100, 80, 0));
		rect.setSize(sf::Vector2f(20, 100));
		window.draw(rect);

		window.display(); //flip the buffer (memory) to the screen

	}//end game loop-------------------------------------------------



	return 'no'; //tell the operating system we finished the program successfully 
} //end main
