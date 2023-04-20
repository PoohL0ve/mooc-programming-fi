# use integer from user as the limit
# print powers of 2 of each number below the limit

limit = int(input('Enter an integer: '))
number = 1
power_of_2 = 0

while number <= limit :
    print(number)
    number = number * 2
print('Done')