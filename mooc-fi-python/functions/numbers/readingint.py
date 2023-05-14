"""
    Function read_input asks the user for an interger between two specified
    integers using a try-except block to handle errors.

    return: return the integer that the user enters once the test is passed
"""
def read_input(number1: int, number2: int) :
    while True :
        try :
            enter = int(input('Please enter an integer: '))
            if enter > number1 and enter < number2 :
                print('A valid number')
                break
        except :
            print('Not a number')
    
    print(f'You entered {enter}') 

# test for function
if __name__ == '__main__' :
    test = read_input(10, 23)
           