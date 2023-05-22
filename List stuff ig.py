#A program that's list practice. Personal challenge: Keep the program equal to 23 lines.
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
def reverse(lis):
    las = []
    for i in range(len(lis)):
        las.append(lis[len(lis)-i-1])
    return las
for i in range(5):
    last = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
    print(last,"\nMax of the list is", max(last),"\nIt is", conse(last), "that the list has at least three consecutive values in it.\nThe list reversed is", reverse(last))
else:
    print("ez")