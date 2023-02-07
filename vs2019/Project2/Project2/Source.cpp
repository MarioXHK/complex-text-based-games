// Demonstrate primitve drawing in SFML
#include<iostream>
using namespace std;


#include "SFML/Graphics.hpp"


class Brick {
public: //All of the program can see and access these
    //functions go here
    Brick(float w, float h, float x, float y);//Constructor
    void draw();
    bool coalcheck(float bx, float by, float bw, float bh);
    void death();
    bool dead();//Return private bool ded
private: //ONLY class members aka those functions up there can see these
    //variables go here
    int width;
    int height;
    int xpos;
    int ypos;
    bool ded;
};




int main() {

    //game set up (you'll need these two lines in every game)
    sf::RenderWindow renderWindow(sf::VideoMode(1000, 600), "Pong Paddle"); //set up screen
    sf::Event event; //set up event queue

    //paddle set up
    sf::RectangleShape paddle(sf::Vector2f(100.0f, 25.0f));
    paddle.setFillColor(sf::Color::Blue); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    paddle.setPosition(550.0f, 550.0f); //set position: this is where the top left corner will be

    //bricks and bracks
    Brick nyan(80.0f, 20.0f, 100.0f, 100.0f);
    Brick rail(60.0f, 20.0f, 300.0f, 100.0f);

    //temp fake things
    sf::RectangleShape nayn(sf::Vector2f(80.0f, 20.0f));
    nayn.setFillColor(sf::Color::Green); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    nayn.setPosition(100.0f, 100.0f); //set position: this is where the top left corner will be

    sf::RectangleShape road(sf::Vector2f(80.0f, 20.0f));
    road.setFillColor(sf::Color::Magenta); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    road.setPosition(300.0f, 100.0f); //set position: this is where the top left corner will be


    //balls
    float ballX = 500;
    float ballY = 300;
    float xVel = .05f;
    float yVel = .05f;
    sf::CircleShape ball(10);
    ball.setFillColor(sf::Color(255, 255, 255));
    ball.setPosition(ballX, ballY);


    //################### HOLD ONTO YOUR BUTTS, ITS THE GAME LOOP###############################################################
    while (renderWindow.isOpen()) {//keep window open until user shuts it down
        while (renderWindow.pollEvent(event)) { //look for events

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                renderWindow.close();

            //KEYBOARD INPUT (just one key to start
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
                paddle.move(-8, 0);
            
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) 
                paddle.move(8, 0);
            
        }
        //physics section :D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D:D
        if (ballY < 0 || ballY > 600) 
            yVel *= -1;
        if (ballX < 0 || ballX > 980)
            xVel *= -1;

        //paddle collision
        if (paddle.getPosition().x - 20 < ballX && ballX < paddle.getPosition().x + 100 && paddle.getPosition().y - 20 < ballY && ballY < paddle.getPosition().x + 25) {
            //cout << "paddle1 collision!" << endl;
            if (yVel > 0) {
                yVel *= -1;
            }
        }

        if (nyan.coalcheck(ballX, ballY, 20.0f, 20.0f))
            nyan.death();
        if (rail.coalcheck(ballX, ballY, 20.0f, 20.0f))
            rail.death();

        ballX += xVel;
        ballY += yVel;
        ball.setPosition(ballX, ballY);

        //render section-----------------------------------------
        renderWindow.clear(); //wipes screen, without this things smear
        renderWindow.draw(paddle); //you gotta drew each object
        if (!nyan.dead())
            renderWindow.draw(nayn);
        if (!rail.dead())
            renderWindow.draw(road);
        renderWindow.draw(ball);
        renderWindow.display(); //flips memory drawings onto screen

    }//######################## end game loop ###################################################################################

    cout << "goodbye!" << endl;
} //end game


Brick::Brick(float w, float h, float x, float y) {
    width = w;
    height = h;
    xpos = x;
    ypos = y;
    ded = false;
}
void Brick::draw() {
    //sfml AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
}
bool Brick::coalcheck(float bx, float by, float bw, float bh) {
    if (xpos - bw < bx && bx < xpos + width && ypos - bh < by && by < ypos + height && !ded) {
        cout << "OWWWWWW" << endl;
        return true;
    }
    return false;
}
void Brick::death() {
    ded = true;
}
bool Brick::dead() {
    return ded;
}