NUM_SQUARES = 64


def square(number):
    out_of_range(number)
    return 2**(number - 1)


def total():
    # squares = [square(x) for x in range(1, NUM_SQUARES + 1)]
    # return sum(squares)
    return 2**(NUM_SQUARES) - 1


def out_of_range(value):
    if value < 1 or value > 64:
        raise ValueError('square must be between 1 and 64')
