
def factorials(n : int) :
    """ Function: takes an intger and returns the factorials as values in a dictionary

    keys: refers to the integers which decrements with each iterations
    values: factorials of the resprective integer. For example 5*4*3*2*1

    return: The function returns a dictionary
    """
    my_multipliers = {}
    for v in range(n, 0, -1) :
        b = v
        t = v - 1
        while t > 0 :
            b = b * t
            my_multipliers[v] = b
            t -= 1
    return my_multipliers    

# test for function 
if __name__ == '__main__' :
    a_number = 5
    print(factorials(a_number))