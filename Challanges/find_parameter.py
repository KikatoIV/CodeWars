def find_perimeter(length, width):
    sqr = (length + width)*2
    return(sqr)

find_perimeter(6, 7)

def addition(num):
    num = num +1
    return num

def next_edge(side1, side2):
    num = (side1 + side2) - 1
    return num

def less_than_or_equal_to_zero(num):
    if(num <= 0):
        return False
    else:
        return True
        