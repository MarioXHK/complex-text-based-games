import random
li = [random.randint(0,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11)]
def bub(last):
    for i in range(len(last)):
        for j in range(len(last)-1):
            if last[j] > last[j+1]:
                a = last[j]
                last[j] = last[j+1]
                last[j+1] = a
    return last
print(li)
li = bub(li)
print(li)