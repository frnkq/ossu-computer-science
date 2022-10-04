user_input = int(input("Enter: "))

print("Pair:---")
print("pwr ", 1)
print("root ", user_input)

for pwr in range(1, 6):
    for root in range(0, user_input):
        if root**pwr == user_input:
            print("Pair:---")
            print("pwr ", root)
            print("root ", pwr)
            break
