# dict minimum based on item val

d = {1:1, 2:2, 3:34, 4:32, 5:0, 6:10}

key_min = min(d, key=d.get)

print(key_min)  # 5 

# ------

def slice_iter_assign():
    l = [1,2,3,4,4,5]

    l[2:4] = iter([10,20]) # NOTE : We can assign iterator to sliced assignments