import Maps
import random

class thing:
    #Setting up collision function!
    def mapcollision(MAP,x,y,h,v,vx,vy,kind,duck = False):
        osimp = ((int((x)/40),int((y)/40),int((x+h)/40),int((y+v)/40),int((x+(h/2))/40),int((y+(h/2))/40)),(int((x+2)/40),int((y+2)/40),int((x+(h-2))/40),int((y+(v-2))/40)),(int((y-20)/40)))
        #Complicated tuple, Explanation: X and Y then First: Oversimplfied then otherway, Otherway meaning the thing plus the player's size.
        #Last part of the tuple is y divided by size 2. First tuple is the real numbers while the second is imperciseness to make physics correct ig
        try:
            if (MAP[osimp[0][3]][osimp[1][0]][1] or MAP[osimp[0][3]][osimp[1][2]][1] or MAP[osimp[0][3]][osimp[0][4]][1]) and vy > -0.1 and (y-v) % 40 <= 5 and kind == 0:
                return True#If the checker is below a block
            if (MAP[osimp[0][1]][osimp[1][0]][2] or MAP[osimp[0][1]][osimp[1][2]][2] or MAP[osimp[0][1]][osimp[0][4]][2]) and vy < 0.1 and kind == 1:
                return True#If the checker is above a block
            if (MAP[osimp[1][1]][osimp[0][0]][4] or MAP[osimp[1][3]][osimp[0][0]][4] or MAP[osimp[0][5]][osimp[0][0]][4]) and vx < 0.1 and kind == 2:
                return True#If the checker is to the right of a block
            if (MAP[osimp[1][1]][osimp[0][2]][3] or MAP[osimp[1][3]][osimp[0][2]][3] or MAP[osimp[0][5]][osimp[0][2]][3]) and vx > -0.1 and kind == 3:
                return True#If the checker is to the left of a block
            if (MAP[osimp[2]][osimp[1][0]][2] or MAP[osimp[2]][osimp[1][2]][2] or MAP[osimp[2]][osimp[0][4]][2]) and duck and kind == 4:
                return True#If the checker is ducking
            if kind == 5 and vy > -0.1 and (y-v) % 40 <= 5:
                if MAP[osimp[0][3]][osimp[1][0]][1] and MAP[osimp[0][3]][osimp[1][2]][1] and MAP[osimp[0][3]][osimp[0][4]][1]:
                    return 2#If the checker is completely on a block
                elif MAP[osimp[0][3]][osimp[1][0]][1] or MAP[osimp[0][3]][osimp[1][2]][1] or MAP[osimp[0][3]][osimp[0][4]][1]:
                    return 1#If the checker is on the edge of a block
        except:
            return False
        return False
    def objcollision(obj1,obj2,kind):
        #It takes 2 object's x, y, h, and v values and turns them into a list in that order, obj1 being the object trying to collide
        if (int(obj1[0]) in range(int(obj2[0]),int(obj2[0]+obj2[2])) or int(obj1[0]+obj1[2]) in range(int(obj2[0]),int(obj2[0]+obj2[2])) or int(obj1[0]+obj1[2]/2) in range(int(obj2[0]),int(obj2[0]+obj2[2]))) and (int(obj1[1]) in range(int(obj2[1]),int(obj2[1]+obj2[3])) or int(obj1[1]+obj1[3]) in range(int(obj2[1]),int(obj2[1]+obj2[3])) or int(obj1[0]+obj1[2]/2) in range(int(obj2[1]),int(obj2[1]+obj2[3]))):
            print("hi")
            print(random.randint(1,10))
            