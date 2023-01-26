//piggy simulator!
//a quick introduction/review of C++ classes!

#include<iostream>
using namespace std;
//standalone function declarations/prototypes would go here too!

//class definition-------------------------------------------
class piggy {
private: //private variables can only be seen/used by members of the class
	int xpos;
	int ypos;
	bool isWalking;
	bool isAsleep;
	int number;
public: //can be seen and used by everything in your program
	piggy(); //default constructor: initalizes all the variables in your pig
	piggy(int num); //parameterized constructor
	void walk();
	void sleep();
	void draw();
};//---------------------------------------------------------


class turtle {
private:
	string color;
	string name;
	int hunger;
	bool isSwimming;
public:
	turtle();
	turtle(string nameu, string colour);
	void whatis();
	void feed();
	void move();
};//


int main() {
	turtle t0("Xander", "Purple");
	turtle t1("Carry","Blue");
	turtle t2("Money", "Purple");
	turtle t3("Seabass", "88");
	turtle t4("Terrif", "Green");
	turtle t5("Miracle", "Yellow");
	char input;
	int thetur;
	while (true) { //game loop!
		cout << "Would you like to (c)heck on your turtles, (f)eed them, or have them (m)ove?" << endl;
		cin >> input;
		switch (input) {
		case 'm':
			cout << "Which turtle?" << endl;
			cin >> thetur;
			switch (thetur) {
			case 1:
				t1.move();
				break;
			case 2:
				t2.move();
				break;
			case 3:
				t3.move();
				break;
			case 4:
				t4.move();
				break;
			case 5:
				t5.move();
				break;
			default:
				t0.move();
				break;
			}
			break;
		case 'c':
			t1.whatis();
			t2.whatis();
			t3.whatis();
			t4.whatis();
			t5.whatis();
			break;
		case 'x':
			t0.whatis();
			break;
		case 'f':
			cout << "Which turtle?" << endl;
			cin >> thetur;
			switch (thetur) {
			case 1:
				t1.feed();
				break;
			case 2:
				t2.feed();
				break;
			case 3:
				t3.feed();
				break;
			case 4:
				t4.feed();
				break;
			case 5:
				t5.feed();
				break;
			default:
				t0.feed();
				break;
			}
			break;
		default:
			cout << "That's not a valid character, try again!" << endl;
			break;
		}
	}
}

//class function definitions AND standalone function definitions go here
piggy::piggy() {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	isAsleep = false;
	isWalking = false;
}

piggy::piggy(int num) {
	xpos = rand() % 600 + 100;
	ypos = rand() % 600 + 100;
	isAsleep = false;
	isWalking = false;
	number = num;
}
void piggy::walk() {
	//randomly move in one of 8 directions when isWalking is true
	if (isWalking == true) {
		xpos += rand() % 10 - 5;
		ypos += rand() % 10 - 5;
		int off = rand() % 100 + 1;

		if (off < 30) { //30% chance walking will turn off each turn
			isWalking == false;
		}
	}
	//10% chance any turn that isWalking will turn ON
	int num = rand() % 100 + 1;
	if (num < 10) {
		isWalking = true;
		cout << "walking!" << endl;
		system("pause");

	}
}
void piggy::sleep() {
	//you do this one!
}


void piggy::draw() {
	//eventually this will hold drawing functions to make it graphical
	cout << "Hello I am pig # " << number << endl;
	cout << "My position is " << xpos << " , " << ypos << endl;
	cout << "I am ";
	if (isAsleep) cout << " asleep." << endl;
	else cout << " not asleep." << endl;
}

/// <summary>
/// //////////////////////////////////////////////////////////////////////////////////
/// </summary>

turtle::turtle() {
	name = "you";
	hunger = 0;
	isSwimming = false;
}

turtle::turtle(string nameu, string colour) {
	hunger = 0;
	isSwimming = false;
	color = colour;
	name = nameu;
}
void turtle::move() {
	isSwimming = true;
	hunger += 5;
	cout << name << " is now swimming around.\n";
}
void turtle::feed() {
	isSwimming = false;
	hunger -= 20;
	cout << "Yummy greens for " << name << "!\n";
}


void turtle::whatis() {
	//eventually this will hold drawing functions to make it graphical
	cout << "Hello I am " << name << endl;
	cout << "My favorite color is " << color << endl;
	cout << "My hunger is " << hunger << endl;
	cout << "I am ";
	if (!isSwimming) cout << "not ";
	cout << "swimming." << endl;
}