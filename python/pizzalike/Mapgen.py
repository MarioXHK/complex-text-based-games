def solidcheck(thing, inv = False):
    #Thing is the thing checked if nonsolid, if inv is true then It'll send the opposite
    nonsolid = {0,3,4,9}
    if not thing in nonsolid:
        if inv:
            return False
        else:
            return True
    else:
        if inv:
            return True
        else:
            return False

def cornerchecker(mop,og,cords):
    mep = [[],[],[]]
    for a in range(3):
        for b in range(3):
            try:
                mep[a].append(mop[cords[0]+a-1][cords[1]+b-1])
            except:
                mep[a].append([1])
    if solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,1]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [6,2]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [7,3]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,3]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,4]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [5,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [4,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [5,3]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [4,3]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [4,1]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0],True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [5,1]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [4,2]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [5,2]
    elif solidcheck(mep[0][1][0], True) and solidcheck(mep[1][0][0], True) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [0,3]
    elif solidcheck(mep[0][1][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0], True) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]):
        return [1,3]
    elif solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0], True) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][1][0], True):
        return [0,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0], True) and solidcheck(mep[2][1][0], True):
        return [1,4]
    
    elif solidcheck(mep[0][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [2,3]
    elif solidcheck(mep[0][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [3,3]
    elif solidcheck(mep[0][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [8,3]
    elif solidcheck(mep[2][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True):
        return [2,4]
    elif solidcheck(mep[2][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]):
        return [3,4]
    elif solidcheck(mep[2][1][0], True)and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True):
        return [9,3]
    
    return og
    
#Generate collisionmap function for maps when you're lazy! goes like [up, down, left, right] Also determines how something should be rendered

def coolgen(mape):
    nonsolid = {0,3,9}
    
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            #Turns the map into a bunch of lists
            ep = []
            ep.append(mape[i][j])
            mape[i][j] = ep
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            for k in range(4):#Sets up the 4 things
                mape[i][j].append(False)
            mape[i][j].append([0,0])
            if mape[i][j][0] in nonsolid:#For when something isn't solid
                if mape[i][j][0] == 3:#special case scenario: platform
                    mape[i][j][1] = True
                continue
            #Now for all the solid things
            if i > 0:
                if mape[i-1][j][0] in nonsolid:#checks if anything is above it
                    mape[i][j][1]=(True)
            if i < len(mape)-1:
                if mape[i+1][j][0] in nonsolid:#checks if anything is below it
                    mape[i][j][2]=(True)
            if j > 0:
                if mape[i][j-1][0] in nonsolid:#checks if anything is to the left of it
                    mape[i][j][3]=(True)
            if j < len(mape[0])-1:
                if mape[i][j+1][0] in nonsolid:#checks if anything is to the right of it
                    mape[i][j][4]=(True)
            if mape[i][j][3] and mape[i][j][4]:
                mape[i][j][5][0] = 3
            elif mape[i][j][3]:
                mape[i][j][5][0] = 0
            elif mape[i][j][4]:
                mape[i][j][5][0] = 2
            else:
                mape[i][j][5][0] = 1
            if mape[i][j][1]:
                mape[i][j][5][1] = 0
                if mape[i][j][2]:
                    mape[i][j][5][0] += 4
            elif mape[i][j][2]:
                mape[i][j][5][1] = 2
            else:
                mape[i][j][5][1] = 1
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            if mape[i][j][0] in nonsolid:
                continue
            mape[i][j][5] = cornerchecker(mape,mape[i][j][5],[i,j])
    
    return mape

#Scans the map for points of interest (searchfor)

def scanspawn(emap, searchfor):
    mapwith = []
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == searchfor:
                mapwith.append([j*40,i*40])#Adds the point of interests
    return mapwith