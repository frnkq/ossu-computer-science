def sum_string(str, current_pos = 0, number_string = '', sum = 0):
    if str[current_pos] != ',':
        number_string += str[current_pos]

    if len(str) - 1 == current_pos:
        if number_string != '':
            sum += float(number_string)
            return sum

    if str[current_pos +1 ] == ',':
        sum += float(number_string)
        number_string = ""

    current_pos += 1
    return sum_string(str, current_pos, number_string, sum)

##Test
strings_of_numbers_separated_by_comma = [
    "123,44,6.5,2,3,5,6,888,9.8,9.0,-1,8288",
    "123,44,6.5,2,3,58,5.3,9.98,6,888,9.8,9.0,-1,8288",
    "12883,44,677.5,2,3,588888000,6,888,9.8,0,-1,8288",
    "1,2,3",
    "4,5,6",
    "9,10,11",
]
arr = strings_of_numbers_separated_by_comma
for i in range(len(arr)):
    sum = 0
    for j in range(0, len(arr[i].split(','))):
        sum += float(arr[i].split(',')[j])
    print(f"String: {arr[i]} \n Sum by Python: {sum}\n Sum by frnkq: {sum_string(arr[i])} \n ")
