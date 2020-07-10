from collections import Counter
comp = lambda a, b: a != None and b != None and Counter(map(lambda x: x*x,a))==Counter(b)

def comp(array1, array2):
    return None not in (array1, array2) and sum([i*i for i in array1]) == sum(array2)
                
def comp(array1, array2):
    if array1 and array2: # If the inputs are valid arrays
        array1 = list(map(lambda x: x**2, array1)) # Squares every value in the array
        array1.sort() # Sorts both arrays
        array2.sort()
    if array1 == array2: # If the arrays are equal
        return True
    else: # Arrays are different
        return False
    elif array1 == array2 == []: # If the arrays are both empty
        return True
    else: # Invalid input
        return False #

a1 = []
a2 = []

print(comp(a1, a2))
