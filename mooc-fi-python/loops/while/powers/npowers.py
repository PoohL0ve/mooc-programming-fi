# let the user input the limit and the base to be used as powers of

limit = int(input('Enter and integer: '))
base = int(input('Enter the base power: '))
print('Limit: ', limit)
print('Base: ', base)
number = 1

while number <= limit :
    print(number)
    number = number * base
print('Done')