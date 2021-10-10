def g():
    i = 0
    while True:
        i+=1
        print('increment')
        yield i

k = g()

print('started')

# for i in range(3):
#    print(next(k))
