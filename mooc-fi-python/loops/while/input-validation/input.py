# the square root function has to be imported for it to work
from math import sqrt
# if the number is below zero: it's invalid
# if it is above zero: it should return the square root
# if the number is zero: program should stop

while True :
    number = int(input('Please enter a number: '))
    if number == 0 :
        break
    if number < 0 :
        print('Inavalid number')
    if number > 0 :
        print(sqrt(number))
print('Exiting...')