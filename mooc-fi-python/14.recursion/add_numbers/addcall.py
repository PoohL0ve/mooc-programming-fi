"""
    The function takes a list of numbers and uses recursion methodology:

    Function stops when the condition is met
"""

def add_number_to_list(numbers : list) :
    # add numbers to the list until the length can be divided by 5
    if len(numbers) % 5 != 0 : 
        # the added numbers should be equal to 1 + the last number
        add_number = numbers[-1] + 1
        numbers.append(add_number)
        add_number_to_list(numbers)
        return numbers

# test for function
if __name__ == "__main__" :
    figures = [2, 4, 10, 23, 46, 7]
    print(add_number_to_list(figures))