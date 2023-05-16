import math 

"""
    Function hypotenuse finds the side of a triangle opposite the the right angle

    return: the square root of the length
"""

def hypotenuse(leg1: float, leg2: float) :
    squared_diagonal = float(leg1 ** 2) + float(leg2 ** 2)
    diagonal_leg = float(math.sqrt(squared_diagonal))
    return diagonal_leg

# test for function
if __name__ == '__main__' :
    my_length = 13
    your_length = 15
    their_length = hypotenuse(my_length, your_length)
    print(their_length)