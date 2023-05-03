
def count_matching_elements(my_matrix : list, element: int) :
    """ Function takes two arguments in the form of a list and an integer:
        It uses two for loops to iterate the list and find any value that
        matches the integer.
        If a match occurs, it uses a variable (times_matched) to store and check 
        the number of occurences 
    """
    times_matched = 0
    for i in my_matrix :
        for value in i :
            if value == element :
                times_matched += 1
    return times_matched   

# testing function
if __name__ == '__main__' :
    two_d_matrix = [[2, 3, 4], [5, 4, 2], [4, 6, 8]]
    print(count_matching_elements(two_d_matrix, 4))   

# Function works with a simple for loop
# It doesn't work with the range function          