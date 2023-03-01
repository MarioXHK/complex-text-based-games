import random
class chicken:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def update(self):
        self.hunger -= 5
        if self.hunger < 30 and random.randrange(0,2) == 1:
            print("bok BOK!")
            return 1
        else:
            return 0
    def feed(self, food):
        self.hunger -= food
        print("peck peck!")
    def pet(self):
        print("HAPPY CHICKEN NOISES :)")
    def printinfo(self):
        print("This chicken's name is", self.name+ ".\nIt has", self.hunger, "hunger.")
chickens = [chicken("Papyrus"),chicken("Nyan"),chicken("qwerty")]
numeggs = 0
choices = {"pet","feed","printinfo"}
valchickens = []
cex = 0
while True:
    print("Here are the chickens:")
    valchickens = []
    for i in range(len(chickens)):
        print(chickens[i].name)
        valchickens.append(chickens[i].name)
    achoice = input("Which do you want to interact with?\n")
    while not achoice in valchickens:
        achoice = input("Could you try again?\n")
    for i in range(len(valchickens)):
        if achoice = valchickens[i]:
            cex = i
    print("What would you like to do with them?")
    bchoice = input("You can pet, feed, or printinfo the chicken")
    if not bchoice in choices:
        print("Invalid choice :D")
    elif bchoice == "pet":
        chickens[cex].pet()
    elif bchoice == "feed":
        cchoice = int(input("How much?\n"))
        chickens[cex].feed(abs(cchoice))
    elif bchoice == "printinfo":
        chickens[cex].printinfo()
    numeggs += chickens[cex].update()