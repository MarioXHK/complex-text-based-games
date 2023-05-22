life = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
def lifecheck(game,l,f):
    counter = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if [i,j] == [0,0]:
                break
            y = l+i
            x = f+i
            if y > len(game)-1:
                y = 0
            elif y < 0:
                y = len(game)-1
            if x > len(game[0])-1:
                x = 0
            elif x < 0:
                x = len(game[0])-1
            if game[y][x] == 1:
                counter += 1
    if counter < 2 or counter > 3 and game[l][f] == 1:
        return 0
    elif counter == 3 and game[l][f] == 0:
        return 1
    else:
        return game[l][f]
oldlife = life
for i in range(len(life)):
    print(life[i])
for i in range(len(life)):
    for j in range(len(life[0])):
        life[i][j] = lifecheck(oldlife,i,j)
for i in range(len(life)):
    print(life[i])