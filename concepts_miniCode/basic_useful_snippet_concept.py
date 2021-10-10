l = [1,2,3,4,5]

s1, s2, s3, s4 = l[:2], l[2:], set(l[:2]), set(l[2:])

print(s1)
print(s2)
print(s3)
print(s4)

#Useful when keys are changing but value (i.e 0) remains same
d = {}.fromkeys([1,2,3], 0)  

print(d)   


#zip
        
def f(r,c):
    print(r,c)

z = [*map(f, *zip(*((r,c) for r in range(1, 3+1) for c in range(1, 4+1))))]
print(z)


