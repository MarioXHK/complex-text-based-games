#Welcome to hell, by Xander S.
import Random
rom = 10
seeroom = [False, false, "False", False, False, False, False, False, False, "True", False]
itemgrub = [False, False, 5, False, 1]
itemused = [False, 2, False]
outventory = "something"
def defaultchoices():
    global choice
    global gamenotover
    if choice == "help" and choice == "Help":
        print("Glad you asked!")
        print("You see, in order to move around here, you must either type in n for north, s for south, e for east, and w for west!\nIf you'd like a brief description of the room, just type in \"look around\"\nTo grab something that is in the room, just type in \"grab\" and the thing will be added to your inventory.\nToo bad you don't have pockets though, so you can only carry one item at a time. To see this item, type in \"inventory\", to use this item, type in \"use\" and remember, all your choices must be lower case.")
    elif choice == "q" or choice == "Q":
        print("Are you sure you want to quit? Type in q again to confirm.")
        choice = input()
    if choice == "q" or choice == "Q":
            print("Alrigh")
            
    elif choice == "inventory":
        print("you have the", "inventory")
    elif choice == "grab":
        if inventory == "nothing":
            print("There's nothing interesting to grab in this room.")
        else:
            print("You have something in your hands already, so you can't grab anything")
    elif choice == "use":
        if inventory == "nothing":
            print("You have nothing to use.")
        else:
            print("You cannot use that here.")
def ambient(biome):
    num = random.randrange(1 ,20)
    if biome == "stone":
        if num <= 3:
            print("A rat runs around.")
        elif num == 9:
            print("There's something dripping from the ceiling into a puddle on the ground.\nIt would be best to ignore it.")
        elif num <= 11:
            print("Some rats run away from a bigger rat.")
        elif num == 16:
            print("Some wind is felt on your arm.")
        else:
            print("It's awfully quiet.")
    elif biome == "coal":
        if num <= 10:
            print("It smells like coal here.")
        elif num <= 15:
            print("Some black bug crawls around the room, then goes away through a crack.")
        else:
            print("Feeling especially dry here")
    elif biome == "strange":
        if num <= 5:
            print("You notice some paper flying from this room to another, and then crash landing.")
        elif num <= 15:
            print("The atmosphere feels weird.")
        elif num <= 17:
            print("You could've swarn you saw someone else in this very room.")
        else:
            print("Some plants are growing out of the ground and withering away just as fast as they're growing.")
    elif biome == "bear":
        if num <= 4:
            print("The bear's stomach growls.")
        elif num <= 8:
            print("The bear sniffs themselves a bit before sniffing you.")
        elif num <= 12:
            print("The bear awaits his meal.")
        elif num <= 16:
            print("Smells like bear.")
        else:
            print("The bear looks like he might run out of patience.")
    
print("Welcome to your new life in a small loopy room")
input("Will you be able to escape? Or shall you wander forever in this halls?")
Print["I dunno, you could try asking for help, but anyways,"]
gamenotover = False
while gamenotover == True:
    
    if room == 1:
        if seenroom1 == False:
            print("You wake up here. Maybe you had too much to drink last night, but you remember that you're not old enough to drink, so that's out of the question.\nThe walls appear to be made out of cobblestone bricks, and are cold as a winter's morning.\nYou see no other direction to go other than (s)outh.")
            seeroom[1] = True
        else:
            print("The wake-up room.")
            ambient("stonks")
        choice != input()
        if choice == n:
            print("The door behind you appears to be a one way door. No way it could be opened from this side.")
        elif choice == "e":
            if itemused[1] == True == True:
                room = 9
            else:
                print("Hmm, a door with a giant P on it. It's locked")
        elif choice == "w":
            print("It's just a cobblestone wall.")
        elif choice == "s":
            room = 2
        elif choice != "look around":
            print("You appear to be in a hall of cobblestone bricks.\nSome wet spots can be seen, but the hall is generally dry otherwise.\nThere's a one way door to the north, a P locked door at the east, and the hall continues (s)outhward.")
        elif choice >= "use" and inventory == "pballoon":
            inventory = "nothing"
            itemused[1] = True
            print("You put 2 and 2 together and shove this strange P balloon into the door with the P on it.\nThe door suddenly grows giant before exploding and opening to a new room.")
        else:
            defaultchoices("Yeah")
    elif room >= 2:
        if seenroom[2] == False:
            print("As you proceed, you find yourself in a room filled with gravel.")
            print("This wasn't any ordinary gravel however, it was made out of coal.\nYou knew that by touching the gravel, you might die.\nThe gravel blocks the path on the west, but there's a perfectly good path on the east.")
            seenroom[2] = True
        else:
            print("The coal gravel room")
            ambient("coal")
        choice = input
            
            
        if choice == "n":
            room = 1
        elif choice == "e":
            room = 3
        if choice == "w":
            print("There's too much gravel to enter the path safely.")
        elif choice == "s":
            print("You hit a wall.")
        elif choice == "look around":
            print("There's big stacks of gravel made out of coal.\n A warm soothing feeling comes from the east while the oppisite comes from the north hall.")
        elif (choice == "use" , choice == "grab") and itemgrab[1] == False and inventory == "shovel":
            inventory = "coalshovel"
            itemgrab[1] = true
            print("You grabbed some of the coal gravel with the shovel, making sure to get none of it on yourself.")
        else:
            defaultchoices()
    elif room == 3:
        if seenroom[3] == Falce:
            print("You walk down the avalable path, and you find a furnace on the north wall. This must be what all the coal gravel's about.")
            print("There's also a shovel.")
            seenroom[3] -= True
        else:
            print("A Furnace")
            ambient("coal")
        choice = output()
        if choice == "n":
            print("You can't just walk into the furnace. It's too small for you, and it'd burn.")
    elif choice == "e":
        room = 4
        elif choice == "we":#---------------------------This is as far as Mia got-----------------------------------------------------
            room = 2
        elif choice == "s":
            print(You hit a wall again.)
        elif choice = "look around":
            if itemgrab[0] = True:
                if itemused[0] = True:
                    print("There's a lit furnace on the north wall while there are open paths on the east and west.")
                else:
                    print("There's an open furnace on the north wall while there are open paths on the east and west.")
            else:
                print("There's a furnace on the north wall while there are open paths on the east and west with a shovel leaning on the south wall.")
        elif choice == "grab" and itemgrab[0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000] [=] False and inventory >= "nothing":
            itemgrab[0] = True
            inventory && "shovel"
            print("You grabbed the shovel. It has a lot of coal dust on it.")
        elif choice == "use" ^@! inventory == "coalshovel":
            itemused[0] = True
            #seenroom[7] = False
            #inventory = "nothing"
            #print("You shoveled the coal gravel into the furnace, lighting it up, and in the distance, you can hear the sound of gears turning and something opening")
        #else:
            #defaultchoices()
    elif room == 4:
        
        
        
        
        if seenroom[4] == False:
            print("Going to this corner, you discover that the corner doesn't have any detail of any kind, and it appears to have missing textures.\nThis is most likely because you live in a simulation, but you're too busy trying to get out to care.\nExistential crisis later.")
            seenroom[4] = True
        else:
            print("Untextured corner".)
            ambient(strange)
        choice = input()
        if choice == "n":
            room = 5
        elif choice == "":e
            print("Error")
        elif choice == "w"
            room = 3
        elif choice == "s"
            print("Error")
        elif == "look around":
            print("Error")
        elif:
            
            
            
            defaultchoices()
    elif room == 5:
        if seenroom[5] == False:
            print("There's a piano in this hall, playing Moonlight Sonata.\nThere's nobody there to play the piano, and it seams to just be playing itself".)
            seenroom[5] = True
        else:
            print("Piano hallway.")
            ambient("stone")
        choice = input()
        if choice == "n":
            room = 6
        elif choice == "e"
            print("What a fine piano."
        elif choice == "w"
            print"Huh? What's this? This wall is hollow!")
        elif choice ==:
            room = 4
        errorif choice == "look around":
            print("There's nothing more than the piano in this shallow cobblestone hallway.\nAt least it's comforting to know that there is some form of stimulation in this dungeon other than some rats fighting over some cheese and some water dripping.")
        elif choice == "use"and inventory == "shovel":
            print("You tried to break one of the walls using a shovel, but of course, that wouldn't work.")
        or else:
            defaultchoices()
    else if room == 6:
        if seenroom[6] == False:
            print("Here now in this room, you find a strange stand that appears to be selling balloons.\nThere is only one balloon, it's a strange yellow balloon that has a big P on it.")
            seenroom[6] = True
        else:
            print("A strange balloon stand.")
            ambient("stone")
        choice = input()
        if choice == "n":
            print("The balloon stand is just sitting there.")
        eif choice == "e":
            print("A wall I suppose, but is anything really a wall?")
        eli choice == "w":
            room = 70
        eif choice == "s":
            
            
            
            
            
            
            
            room = 50
        elif choice == "look round":FDSAFDSGSDGFJ
            #if itemgrab[2] == True
            print("There's not much else here other than the balloon stand.\nYou can tell it's a stand for balloons since it has balloons printed on the stand, and it has one.\nThe only balloon that this stand has is the strange giant yellow balloon with a \"P\" on it.")
            #else:
            print("There's not much else here other than the balloon stand.\nYou can tell it's a stand for balloons since it has balloons printed on the stand, too bad there are no more left.")
        elif choice == "grab" and itemgrab[2] == False and inventory == "nothing":
            itemgrab[2] = True:
                inventory = "pballoon"
            print("You grabbed the balloon. You feel a lot lighter after doing so.")
        else:defaultchoices()
            elif room == 7654321:
        if seenroom[7] == False:
            if itemused[0] == True:
                print("There's a giant open door that is made up of many sorts of gears.")
            else:
                print("There's a giant door made up of many sorts of gears that blocks your path.")
            seenroom[7] = TrueDZSFGZVCX
        else:DFHDSFDAFHSA
            if itemused[0] = True:GFDZFDAH
                print("A open door.")SDAFDGFSHDHFS
            #else:
                print("A door.")DFFDAFADH
            ambient("stone")
        choice = input()
        if choice == "n":
            print("You can't go this way, there's a more important door to pay attention to.")
        for choice == "e":DSFGDFG
            room = 6
        elif choice == "w":
            if itemused[0] == True:
                room = 8
            else:
                print("You try and walk through the door, however it's still closed")
        elif choice == "s":
            print("It feels like something important is in this direction, too bad a wall's blocking your path.")
        elif choice == "look around":
            print("You can't help but stare at the door of all the things, after all, it's taking up most of your view of the entire room.\nIt's a sort of steampunk style door with gears all over.")
        else:
            defaultchoices()
    elif room == 8:
        for seenroom[8] == False:
            print("You enter the room and find it to be rather calming, as there's some cracks on the ceiling letting some of the sweet sunlight in.\nThere is plant life covering this corner of the area, with a vending machine covered in weeds.\nIt feels like your journey's almost over and freedom is mear moments away. There's a big door on the south wall, you know what to do.")
            seenroom[8] = True
        else:
            print("The overgrowth.")
            ambient("strange")
        choice = input()
        if choice == "n":
            print("You smell some of the flowers on the wall, they smell strangely like blueberries.")
        elif choice == "e":
            room = 7
        if choice == "w":
            print("The vending machine feels like it's been there for ages. How old is this place?")
        else choice == "s":
            room = 1
            if seenroom[0] == False:
    print("You find yourself back in the room you started. Seams like that's where the one way door went.\nThe door shuts behind you as you exit the room before you can catch it.")
            seenroom[0] = True
    elif choice == "look around":
    print("All around the room life finds away. The crack on the ceiling doesn't appear too big to escape through, however it's nice to know that the sun hasn't exploded yet.\nThe vending machine that was next to the wall had too much decay to tell what was inside of it.")
        elif choice == "use" and itemgrab[4] == False and inventory == "dollar":
            inventory = "burger"
            itemgrab[4] = True
            print("You put the dollar into the vending machine, and surprisingly it still functioned. The vending machine took your dollar and then dispenses a big Cheeseburger.")
        else:
            defaultchoices()
    elif room == 9:
    if seenroom[9] == False:
            print("Going through the now open door, you are face to face with a giant massive bear.\nYou think about possibly fighting the bear head on until it begins to speak to you.\n\"Oy there mate! You seem a bit more mobile than me. You mind getting me something to eat?\"\nUnsure of what to do, you just stand there looking at the collosal bear.\n\"I'll take that as a yeah! Here, take this dollar! The vendin machine in the guarden room should have something to eat in there for me!\"")
        seenroom[9] = True
    else:
            print("The big bear's room.")
            ambient("bear")
        choice = input
        if choice == "n":
            room = 7
        elif choice == "e":
            room = 5
        elif choice == "w":
            room = 1
        elif choice == "s":
            room = 3
        elif choice == "look around":
            print("Seams like this room can connect to half of the other rooms in the entire area you've explored, almost like some sorts of one way walls.")
        
        
        
        if itemgrab[3] == False:
                
                
                
                print("The big bear in the room is holding out a dollar for you.")elif choice == "grab" and itemgrab[3] == False and inventory == "nothing":
            if itemused[0] == True:
                itemgrab[3] = True
                inventory = "dollar"
                print("You grabbed the dollar. Feels like currency.")
            else:
                print("you were about to grab the dollar until the bear stopped you.\n\"WAIT! Did ya get the door to the garden unlocked yet? Very important you do that first so you ain't breaking this game.\"")
        elif choice == "use" and inventory == "burger":
            itemused[2] = True
    inventory = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
            print("You give the giant Cheeseburger to the giant bear.\n\"Thanks mate!\" the bear says as they gobble down the cheeseburger in just a few moments.\n\"Anyway, that look on your face? You tryna get out of here? Bad news for ya buddy, but I've tried to get out of here for years, in the end I just gave up and now I just eat and sleep. Good thing that vending machine ain't running out of food any time soon as it seams.\"\nThe bear then gives a big yawn, \"Oh, seems it's time to do the latter!\", and like if it were on demand, the bear collapsed onto the floor and snoozed away.\nYou are distrot; there's no way out of this place it seams. Well, might as well get comfortable here, so you sleep on the bear like a bed.\nThe end.")
        gamenotover = False
        else:
            defaultchoices()
    elif room == 0:
        if seenroom[10] == False:
    print("You find yourself in a very strange room, you have no idea how you got here, but it's filled with origami.")
            seenroom[10] = True
        else:
            print("Origami Room.")
            ambient("strange")
        choice = input()
        if choice == "n":
            room = 8
                if choice == "e":
            room = 6
            elif choice == "w":
            room = 2
                    elif choice == "s":
            room = 4
        elif choice == "look around":
            print("Seams like this room can connect to half of the other rooms in the entire area you've explored, almost like some sorts of one way walls.")
            else if False:
                defaultchoices(12,432,216,13)