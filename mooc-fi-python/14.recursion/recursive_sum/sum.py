"""
    Function: A recursive function
    condition:
    variable: sum_of_values used to add all the number together
    return: The sum of all the numbers in the range of the given number
"""
def recursive_sum(number : int) : 
    if number <= 1 :
        return number
    return recursive_sum(number - 1) + number

# test for function
if __name__ == "__main__" :
    result = recursive_sum(5)
    print(result)