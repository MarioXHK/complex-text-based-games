import random
def ohf(numb):
    print(numb, "to be !'d")
    if numb > 0:
        for i in range(numb-1,0,-1):
            numb *= i
        return numb
    if numb < 0:
        numb = abs(numb)
        for i in range(numb-1,0,-1):
            numb *= i
        return 0-numb
    return 1

def ohfrec(numb):
    print(numb, "to be !'d recursively")
    negative = False
    if numb < 0:
        negative = True
        numb = abs(numb)
    thinger = numb * (numb-1)
    if thinger > 1:
        numb = thinger * ohfrec(numb-2)
    if numb < 1:
        numb = 1
    return numb
    

    


def lully(nur):
    print(nur, "to be added numbers")
    stri = []
    stri.extend(str(nur))
    elo = 0
    for i in stri:
        elo += int(i)
    return elo


def lullyrec(nur):
    print(nur, "to be added numbers recursively")
    thingtomurder = 10**(len(str(nur))-1)
    thingtoadd = 0
    while nur - thingtomurder >= 0:
        thingtoadd += 1
        nur -= thingtomurder
    if nur == 0:
        return thingtoadd
    else:
        return lullyrec(nur) + thingtoadd
        
        


def nature(nah):
    print(nah, "to be doing the natural number trip")
    uh = 0
    for i in range(1, nah+1):
        uh += i
    return uh




def naturerec(nah):
    print(nah, "to be doing the natural number trip recursively")
    thing = nah-1
    if thing > 0:
        nah += naturerec(thing)
    return nah

def power(ay,bee):
    print(ay, "to the", bee, "powering")
    return (ay ** bee)
def powerrec(ay,bee):
    print(ay, "to the", bee, "powering recursively")
    sea = 1
    bee -= 1
    if bee > -1:
        sea = ay * powerrec(ay,bee)
    return sea
    


print("Henlo")
for j in range(10):
    print(ohf(j))
for j in range(10):
    print(ohfrec(j))
print(lully(random.randrange(1,1000000)))
print(lully(12345))
print(lullyrec(12345))
print(nature(15))
print(naturerec(15))
print(power(5,4))
print(powerrec(5,4))