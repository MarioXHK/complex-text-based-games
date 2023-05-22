#thing for thing 6

class fruit:
    def __init__(self,t,w):
        self.type = t
        self.weight = w
        self.isFresh = True
    def printinfo(self):
        print("This fruit is a", self.type, "type fruit that weighs", self.weight, "grams. It is", end = " ")
        if not self.isFresh:
            print("not", end = " ")
        print("fresh")
    def turnrotten(self):
        self.isFresh = False
        print("Blegh-")
    

#things for thing 4

def AvgTwoNums(x,y):
    return (x+y)/2
def GiveCompliment(name):
    print(name+", you look so more than average today!")

#program starts here!

print("I'm a cat")

#Thing 1

blb = int(input("how much can you bench press?\n"))
if blb < 10:
    print("Hmm... Maybe u should practice to get buffff1")
elif blb >= 10 and blb <= 50:
    print("O u doing good, u getting swol!")
else:
    print("Oh heavens that's a lot of muscleeeeeeeeeeeee u very SWOL.")
#rating: 5

#Thing 2
for i in range(20,51,2):
    print(i, end=" ")
print()
oop = "h"
#rating: 5

#thing 3

while oop != "frog":
    oop = input("Hop...\n")
print("Not a frog, a rabbti... No wai I'm a cta")
#rating: 5

#thing 4

for a in range(9):
    print(AvgTwoNums(a,4))
wiz = "the you"
while wiz != "you":
    wiz = input("What's ur name?\n")
    if wiz == "you":
        wow = input("What? No hey wait a minute... You can't be you, I'm me... Btw why do they call it an oven?\n")
        if wow == "when you of in the cold food of out hot eat the food?":
            print("That's what I'm saying!")
        else:
            print("Wrong")
    else:
        GiveCompliment(wiz)
#rating: 5

#thing 5

marbles = [4,6,2,9]
print(marbles)
print(marbles[1])
for b in range(len(marbles)):
    marbles[b] *= 5
print(marbles)
#rating: 5

#thing 6

paper = fruit("Cherry", 54)
thing = fruit("Apple",9362754)
paper.printinfo()
thing.printinfo()
paper.turnrotten()
thing.turnrotten()
paper.printinfo()
thing.printinfo()

#rating: 4.9 (I forgot the defs at the beginning of the class functions :( but I did do it all the second try.)