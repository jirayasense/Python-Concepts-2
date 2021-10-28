import itertools as it

def skip(l, skip=0):
    i = 0
    while(i != skip):
        i += 1
    while i < len(l):
        yield l[i]
        i += 1

l = [1,2,3,4,5,6]
#rpl2 = list(skip(l, 2))
print(list(skip(l, 2)))  # [3,4,5,6]
print('Over')
