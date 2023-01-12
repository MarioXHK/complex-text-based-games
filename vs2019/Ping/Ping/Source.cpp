// Demonstrate primitve drawing in SFML
#include<iostream>
using namespace std;


#include "SFML/Graphics.hpp"

int main() {

    //game set up (you'll need these two lines in every game)
    sf::RenderWindow renderWindow(sf::VideoMode(1000, 600), "Pong Paddle"); //set up screen
    sf::Event event; //set up event queue

    //paddle1 set up
    sf::RectangleShape paddle1(sf::Vector2f(25.0f, 150.0f));
    paddle1.setFillColor(sf::Color::Blue); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    paddle1.setPosition(50.0f, 200.0f); //set position: this is where the top left corner will be
    sf::RectangleShape paddle2(sf::Vector2f(25.0f, 150.0f));
    paddle2.setFillColor(sf::Color::Red);
    paddle2.setPosition(925.0f, 200.0f);

    float ballX = 500;
    float ballY = 300;
    float xVel = .01;
    float yVel = .01;

    sf::CircleShape ball(25);
    ball.setFillColor(sf::Color(127, 0, 255));
    ball.setPosition(ballX, ballY);


    //################### HOLD ONTO YOUR BUTTS, ITS THE GAME LOOP###############################################################
    while (renderWindow.isOpen()) {//keep window open until user shuts it down
        while (renderWindow.pollEvent(event)) { //look for events

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                renderWindow.close();

            //KEYBOARD INPUT (just one key to start
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::W)) { //checks if "W" is pressed
                paddle1.move(0, -5); //move the rectangle 5 pixels UP on the y axis
            } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) { //checks if "S" is pressed
                paddle1.move(0, 5); //move the rectangle 5 pixels DOWN on the y axis
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
                paddle2.move(0, -5);
            }
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
                paddle2.move(0, 5);
            }
        }
        //physics section :D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D
        if (ballY < 0 || ballY > 550) {
            yVel *= -1;
        }
        //paddle collision
        if (ballX - 25 < paddle1.getPosition().x && ballY > paddle1.getPosition().y && ballY < paddle1.getPosition().y + 100) {
            cout << "paddle1 collision!" << endl;
            xVel = .01;
        }
        if (ballX + 25 > paddle2.getPosition().x && ballY > paddle2.getPosition().y && ballY < paddle2.getPosition().y + 100) {
            cout << "paddle2 collision!" << endl;
            xVel = -.01;
        }
        ballX += xVel;
        ballY += yVel;
        ball.setPosition(ballX, ballY);
        //render section-----------------------------------------
        renderWindow.clear(); //wipes screen, without this things smear
        renderWindow.draw(paddle1); //you gotta drew each object
        renderWindow.draw(paddle2);
        renderWindow.draw(ball);
        renderWindow.display(); //flips memory drawings onto screen

    }//######################## end game loop ###################################################################################

    cout << "goodbye!" << endl;
} //end game