
def double_items(numbers : list) :
    """ Function takes a list as an argument and returns a new list by 
        doubling the integers in original list without altering the original list.

        new_list : contains the returned values
        numbers : contains the original values
    """
    new_list = []
    for item in numbers :
        new_list.append(item * 2)
    return new_list

# test for the function
if __name__ == '__main__' :
    my_numbers = [1, 2, 3, 4]
    doubled_numbers = double_items(my_numbers)

    print(f'Original List: {my_numbers}')
    print(f'Doubled List: {doubled_numbers}')
