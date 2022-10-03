x, y, z = 8, 9, 1
greatest = x if (x > y and y > z) else y
greatest = y if y > z else z

if greatest % 2 == 0:
    print(greatest)
else:
    print("No odd numbers")
