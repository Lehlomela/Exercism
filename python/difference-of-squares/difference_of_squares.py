# todo:: research and redo

def square_of_sum(number):
    sum_of_nums = sum([x for x in range(1, number + 1)])
    return pow(sum_of_nums, 2)

def sum_of_squares(number):
    squares = [pow(x, 2) for x in range(1, number + 1)]
    return sum(squares)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
