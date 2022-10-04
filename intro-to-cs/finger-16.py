remaining_inputs = 3
largest = None

while remaining_inputs:
    current_input = int(input("Enter integer: ") )
    current_is_odd = current_input % 2 != 0

    if largest == None:
        largest = current_input
    if current_input > largest and current_is_odd:
        largest = current_input

    remaining_inputs -= 1

if largest % 2 != 0:
    print("Largest: ", largest)
else:
    print("No odd numbers were provided")

