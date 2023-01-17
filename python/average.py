def averageig(theit):
    itit = 0
    for i in range(len(theit)):
        itit += theit[i]
    avg = itit / len(theit)
    return avg
def ezavrage(theit):
    itit = 0
    avg = sum(theit)/len(theit)
    return avg
listy = [4,5,2,6,1,6,7,9,1,2,3,7,8,1,2,3,5,9,10,6,77,32,24,1,32,21,1,2,1,51,5,12,12,51]
print(listy)
print(averageig(listy))
print(ezavrage(listy))