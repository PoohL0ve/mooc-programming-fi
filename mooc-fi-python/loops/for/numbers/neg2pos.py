# let user enter a positive integer
# print from the negative equivalent to the specified number

user_number = int(input('Enter a positive integer: '))
number = user_number + 1

for figure in range(-user_number, number) :
    if figure == 0 :
        continue
    if figure != 0 :
        print(figure)