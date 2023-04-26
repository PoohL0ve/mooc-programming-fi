# return the range of a list

def range_of_list(numbers : list) :
    largest = max(numbers)
    smallest = min(numbers)
    the_range = largest - smallest
    return the_range

# test for function
my_figures = range_of_list([120, 345, 789, 457])
print(f'The range of the numbers is {my_figures}')