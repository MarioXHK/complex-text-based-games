import random
def conse(lis):
    lis.sort()
    counter = 0
    for i in range(len(lis)):
        if i+1 != len(lis) and lis[i] + 1 == lis[i+1]:
            counter += 1
        else:
            counter = 0
        if counter >= 3:
            return True
    return False
last = []
for i in range(12):
    last.append(random.randint(1,10))
print(last)
last.sort()
print(last)
print(max(last))
print("The list does", end = " ")
if not conse(last):
     print("not", end = " ")
print("have at least three consecutive values in it")