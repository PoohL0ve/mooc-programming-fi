
def times_ten(start_index : int, end_index: int) :
    """ Function takes two integers as an argument and returns a dictionary

        keys : values obtained from the first integer and includes the last
        values : keys times 10
        The for loop with the range is used to iterate the arguments, then add the
        calculations to the dictionary using bracket notation. 
    """
    my_values = {}

    for v in range(start_index, end_index + 1) :
        my_values[v] = v * 10
    return my_values

#test function
if __name__ == '__main__' : 
    figure_one = 2
    figure_two = 4
    times_ten(figure_one, figure_two)