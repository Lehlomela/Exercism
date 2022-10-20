def is_armstrong_number(number):

    # sum = 0
    # for digit in str(number):
        # sum += int(digit) ** len(str(number))
        
    # return number == sum

    str_num = str(number) # num to string
    pow = len(str_num)
    return sum([int(x) ** pow for x in str_num]) == number