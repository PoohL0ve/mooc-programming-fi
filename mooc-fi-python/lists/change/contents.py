# create a list with numbers 1, 2, 3, 4 and 5
# let the user enter and index and a new value
# replace the value stored at the index entered by the user with the new value
# if -1 is entered, end the loop

my_list = [1, 2, 3, 4, 5]

while True :
    index = int(input('Enter a number between 1 and 4 or -1 to end: '))
    value = int(input("Enter any value: "))

    if index > -1 :
        my_list[index] = value
        print(f'Index: {index}')
        print(f'New Value: {value}')
        print(my_list)
    if index == -1 :
        break
print(f'Fun is over')