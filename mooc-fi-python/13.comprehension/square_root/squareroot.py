from math import sqrt
""" The function takes a list of inters and returns a list using the comprehension method

    The list return contains the squaroot of the numbers found in the original list
"""
def square_root(figures: list) :
    new_figures = [sqrt(number) for number in figures]
    return new_figures

# test for the program
if __name__ == "__main__" :
    my_numbers = [4, 9, 16, 25, 36, 49]
    print(square_root(my_numbers))
