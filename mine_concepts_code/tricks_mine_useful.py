# dict minimum based on item val

d = {1:1, 2:2, 3:34, 4:32, 5:0, 6:10}

key_min = min(d, key=d.get)

print(key_min)  # 5 