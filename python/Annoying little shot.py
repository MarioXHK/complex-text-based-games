import random
umm = True
def what(name):
    ohfu = random.randrange(1,101)
    if ohfu < 25:
        print("Awww UNCLE please? I want to challenge this GYM!")
    elif ohfu < 60:
        print("UNCLE, I'll go back to verdanturf.")
    elif ohfu < 80:
        print("oh wow a pokemon!")
    else:
        print("OH", name, "it's me, WALLY!")
        return False
    return True
print("Enter ur name")
player = input()
while umm:
    umm = what(player)