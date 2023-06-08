""" The function takes two arguments: 
    first argument: a list
    second argument: an integer
    return: a new list based on the integer by removing values smaller than 
    the value specified by the integer
"""
def remove_smaller_than(numbers: list, figure: int) :
    smaller_list = [item for item in numbers if item > figure ]
    return smaller_list

# test for code
if __name__ == "__main__" :
    group_score = [34, 56, 99, 54, 23, 12]
    nombre = 45
    print(remove_smaller_than(group_score, nombre))