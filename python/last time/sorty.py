import random
def sorting(thelist):
    newlist = []
    for o in range(len(thelist)):
        jek = 0
        for i in range(len(thelist)):
            if i != 0:
                if thelist[jek] > thelist[i]:
                    jek = i
        newlist.append(thelist.pop(jek))
    return newlist

def sortsec(thelist):
    for o in range(len(thelist)):
        jek = 0
        for i in range(len(thelist)):
            if i != 0:
                if thelist[jek] > thelist[i]:
                    jek = i
        temp = thelist[o]
        thelist[o] = thelist[jek]
        thelist[jek] = temp
    return thelist

def shuffle(alist):
    for y in range(len(alist)):
        eff = random.randrange(0, len(alist))
        alist[y], alist[eff] = alist[eff], alist[y]
    return alist

def examplesort():
    numlist = [6,4,3,2,7,62,16,85,21]
    anolist = [23476,321,112,11,12,3,5176,32,724,2,3,5,1,7,8,9,61,1,2,3,5,9,21,113,73,12,123,62,171]
    lastlist = [random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20),random.randrange(0, 20)]
    print(numlist)
    numlist = sorting(numlist)
    print(numlist)
    print(anolist)
    anolist = sorting(anolist)
    print(anolist)
    print(lastlist)
    lastlist = sorting(lastlist)
    print(lastlist)
    print(numlist)
    numlist = shuffle(numlist)
    print(numlist)
    print(anolist)
    anolist = shuffle(anolist)
    print(anolist)
    print(lastlist)
    lastlist = shuffle(lastlist)
    print(lastlist)
def bubbler(bellist):
    for i in range(len(bellist)):
        for i in range(len(bellist)):
            if i != len(bellist)-1:
                if bellist[i] > bellist[i+1]:
                    temp = bellist[i+1]
                    bellist[i+1] = bellist[i]
                    bellist[i] = temp
    return bellist

yourlist = []
listsize = int(input("HOw long list?"))
for i in range(listsize):
    yourlist.append(random.randrange(1, 101))
print(yourlist)
yourlist = bubbler(yourlist)
print(yourlist)