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

s = "1.23,2.4,3.123,8999992828982.555"
sum = sum_string(s)
print("Sum: ", sum)
