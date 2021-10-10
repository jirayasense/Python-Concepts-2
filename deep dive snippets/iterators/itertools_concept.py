import itertools as it 
import math

# 1 islice amazing concept

def factorials():
    i = 1
    while True:
        print('-> yielding ', i)
        yield math.factorial(i)
        i += 1

l = list(it.islice(factorials(), 2, 5))
print(l)
''' (Output)notice factorials() is iterated from 0 -> 5 entirely, though we demanded 2 -> 5
-> yielding  1
-> yielding  2
-> yielding  3
-> yielding  4
-> yielding  5
[6, 24, 120]
'''

# Numerical or Float Step-Size
l = it.count(3, 0.5)  # -> returns iterator so no need to call iter()
l2 = [next(l) for _ in range(3)]  

print(l2)  # [3, 3.5, 4.0]


# Another way 
l = it.count(3, 0.5)
print(*it.islice(l, 3))  # 3 3.5 4.0   //Equivalent ob above but much concise way


