def leap_year(year):
    if (evenly_divisible(year, 100) and not evenly_divisible(year, 400)):
        return False

    if (evenly_divisible(year, 4)):
        return True
    
    return False


def evenly_divisible(year, number):
    return year % number == 0