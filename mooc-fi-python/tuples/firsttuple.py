"""
    Function creates a tuple based on:

    arguments: 3 integers
    program: organise the arguments in order of smallest, largest and sum
    return: return a tuple with the criteria from the program mentioned above
"""
def create_tuple(x: int, y: int, z: int) :
    check_list = [x, y, z]
    order_list = sorted(check_list)
    smallest = order_list[0]
    largest = order_list[2]
    total = sum(order_list)
    first_tuple = (smallest, largest, total)

    return first_tuple

#test for tuple creation
if __name__ == '__main__' :
    print(create_tuple(23, 5, -4))