import random
def MonsterGenerator():
    zed = random.randrange(0,10)
    if zed < 2:
        print("Skeleton")
    elif zed < 5:
        print("Zombie")
    elif zed < 6:
        print("Witch")
def AddTwoDivideSix(a,b):
    return (a+b+2)/6
oo = "e"
while oo != "quit":
    oo = input()
    print(AddTwoDivideSix(random.randrange(1,20),random.randrange(1,20)))
    MonsterGenerator()
print(AddTwoDivideSix(5.0,2.5))