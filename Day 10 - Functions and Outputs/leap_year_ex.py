def is_leap_year(year):

    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 400 == 0) and (year % 100 != 0):
        return True
    else:
        return False
    
print(is_leap_year(1989))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)