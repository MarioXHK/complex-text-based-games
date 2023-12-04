import random

cnames = ("U","Flip","Metala","Transformed U","Flip Construct","Royapi","Toito","Bee","Noteling","Shapebro","Sharpbro","Icingbro","Lucking","Unlucking","Metalface")

cdescr = ("The U are a perculiar species that enhabit just about\nevery place sunlight can see. Coming in many different\nshapes and sizes, they have a variety\nof abilities, however you got a regular U.\n",
          "Flips are often found in abandoned office buildings\nsince they have an abundance of paper there.\nFlips are formed from special flip particles landing on\nfoldable paper, which then folds to form the flip shape.\n",
          "Metala are born when a metala pearl lands on a piece of\nscrap metal. They float steadily in the air and\npossess abilities to make others float as well.\n",
          "Us often like to go into objects. These transformed Us\ndisquise most of the time in the environment,\nhoping that a prey item will fall for the trap or\nnot even notice the U at all!\n",
          "A collection of flips can create one giant flip or flip\nconstruct. They can scare predators and sometimes\neven erupt into wirlwinds.\n",
          "Royapi are royal Metala that control royal types of metal\npieces like a crown or staff. Because of the piece\nof metal they're possessing is of royalty\nit might have a grand history with all sorts\nof things hidden in them.",
          "Toitos are innocent plush heads with an immesurable string\nattached to them.\nIf this string were to break, the \nToito would die easily.\n",
          "Bees are aliens from another world that have landed in\nthis world from bad luck. Their ship of origin is long\ngone and now these Bees have permanently\nbeen intigrated into the environment.\n",
          "When a bunch of notelings come together it's called music.\nWhen a bunch of Us come together it's called a sentence.\nBut the music would win since it holds\nmuch more information in so little.\n",
          "Shapebros are creatures that are made up of one shape.\nSuch bouncy creatures with such personality. Unfortunately\nThey are at the bottom of the food chain\nbecause of choosing social things instead\nof doing survival things.",
          "Sharpbros are shapebros that chose violence. They use\ntheir shapes to bash anyone in their way.\n",
          "Icingbros are shapebros that are a lil different and\nthus are socially isolated from every other one of it's kind.\nIt's a pure survival machine because\nof this, and it would probably do a murder.\n",
          "Luckings are products of the giant luck structure in\nthe sky. They try and bring luck and joy to all the good\nboys and girls. Because of their lucky effects\nthey aren't actually a part of the food\nchain since everyone, even carnivores\nwant a piece of dat luck.\n",
          "Unluckings are products of the giant unluck structure\nin the sky. They go around scaring everyone and\nruining the luck of people. Because of this\nthey aren't welcome in any ecosystem, but nobody's\n afraid of kicking them out, since they\nmight just run out of luck.",
          "Metalfaces are usually on the front of important\nbuildings. They guard and frown upon those who dare enter\nwithout permission.\n")

defstats = [
    [23,16,12,19], #0: the U
    [16,13,15,20], #1: Flips
    [19,10,18,12], #2: Metalas
    [30,18,21,17], #3: Transformed Us
    [26,20,15,24], #4: Flip Constructs
    [23,20,22,19], #5: Royapis
    [21,16,13,12], #6: Toitos
    [19,14,10,17], #7: Bees
    [15,15,6,22], #8: Notelings
    [18,10,13,14], #9: Shapebros
    [18,17,12,11], #10: Sharpbros
    [16,13,20,18], #11: Icingbros
    [], #12: Luckings
    [], #13: Unluckings
    [], #14: Metalfaces
    [], #15: Sand Octopuses
    [],
    []
]
types = {
"rock" : ["rock",0,3,11],
"paper" : ["paper",1,4,8,9],
"scissors" : ["scissors",2,5,7,10],
"aerial" : ["aerial",1,4,5],
"meat" : ["meat",0,6,9,15],
"tech" : ["tech",14],
"myth" : ["myth",12],
"spirit" : ["spirit",13],
"physics" : ["physics",15]
}

class creature:
    def __init__(self,id: int, lvl: int, wild: bool = False):
        global cnames
        global defstats
        self.name = cnames[id]
        self.id = id
        self.lvl = lvl
        self.wild = wild
        self.stats = defstats[id]
        if self.wild:
            self.lvl += random.randint(-5,5) 
        if self.lvl < 1:
            self.lvl = 1
        self.xp = int((self.lvl*5)**1.3)
        for i in range(lvl):
            for j in range(4):
                k = random.randint(0,3)
                if k == 0:
                    k = 2
                self.stats[j] += k
        self.tempstats = self.stats
    def printInfo(self):
        global cnames
        global cdescr
        global types
        print(cnames[self.id], end = "")
        if cnames[self.id] != self.name:
            print(" \"" + self.name + "\"", end = "")
        print("\nLevel:", self.lvl,"\nXP till next level:", self.xp,"\nHP:", self.stats[0],"\nAttack:", self.stats[1],"\nDefense:", self.stats[2],"\nSpeed:", self.stats[3],"\nTypes:")
        if self.id in types["rock"]:
            print("Rock,", end = " ")
        if self.id in types["paper"]:
            print("Paper,", end = " ")
        if self.id in types["scissors"]:
            print("Scissors,", end = " ")
        if self.id in types["aerial"]:
            print("aerial,", end = " ")
        if self.id in types["meat"]:
            print("Meaty,", end = " ")
        if self.id in types["tech"]:
            print("Technic,", end = " ")
        if self.id in types["myth"]:
            print("Mythical,", end = " ")
        if self.id in types["spirit"]:
            print("Spiritual,", end = " ")
        if self.id in types["physics"]:
            print("Physics-based,", end = " ")
        print("\nDescription:\n"+ cdescr[self.id])
    def printBattleInfo(self):
        print("HP:", self.tempstats[0],"\nAttack:", self.tempstats[1],"\nDefense:", self.tempstats[2],"\nSpeed:", self.tempstats[3])
    def giveXP(self,amount):
        self.xp -= amount
        if self.xp <= 0:
            self.xp += int((self.lvl*5)**1.3)
            for j in range(4):
                i = random.randint(0,3)
                if i == 0:
                    i = 2
                self.stats[j] += i
    def attack(self,them,power) -> int:
        global types
        crit = random.randint(1,6)
        if crit == 1:
            crit = 2
        else:
            crit = 1
        fd = (2*self.lvl)/5+2
        sadamage = ((fd*power.p*(self.tempstats[1]/them.tempstats[2]))/5)*crit+2


        #Types + weaknesses

        if moveTypeCheck(power,types, "rock"): #rock type
            if them.id in types["scissors"] or them.id in types["aerial"]:
                sadamage *= 1.2
            if them.id in types["paper"] or them.id in types["tech"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "paper"): #paper type
            if them.id in types["rock"] or them.id in types["spirit"]:
                sadamage *= 1.2
            if them.id in types["scissors"] or them.id in types["aerial"]:
                sadamage *= 0.8
                        
        if moveTypeCheck(power,types, "scissors"): #scissors type
            if them.id in types["paper"] or them.id in types["meat"]:
                sadamage *= 1.2
            if them.id in types["rock"] or them.id in types["aerial"] or them.id in types["tech"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "aerial"): #air type
            if them.id in types["paper"] or them.id in types["physics"]:
                sadamage *= 1.2
            if them.id in types["rock"] or them.id in types["scissors"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "meat"): #meat type
            if them.id in types["paper"]:
                sadamage *= 1.2
            if them.id in types["rock"] or them.id in types["tech"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "tech"): #tech type
            if them.id in types["meat"] or them.id in types["physics"]:
                sadamage *= 1.2
            if them.id in types["myth"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "myth"): #mythic type
            if them.id in types["spirit"] or them.id in types["tech"]:
                sadamage *= 1.2
            if them.id in types["physics"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "spirit"): #spirit type
            if them.id in types["spirit"] or them.id in types["paper"]:
                sadamage *= 1.2
            if them.id in types["tech"] or them.id in types["meat"]:
                sadamage *= 0.8
        
        if moveTypeCheck(power,types, "physics"): #spirit type
            if them.id in types["rock"] or them.id in types["meat"]:
                sadamage *= 1.2
            if them.id in types["tech"]:
                sadamage *= 0.8

        damage = sadamage + (random.randint((0-self.lvl),self.lvl)/2)
        
        return int(damage)

def moveTypeCheck(power,typing: dict,check) -> bool:
    for i in power.type:
        if i in typing[check]:
            return True
    return False

class move:
    def __init__(self,power: int,tipes: tuple,specials: list = []):
        self.p = power
        self.type = tipes
        self.sa = specials #short for special abilities
