# ask the uses for the number of items in a list
# let the user give the values for the list

my_list = []
number = int(input('Enter a number to build a list: '))

while number > 0 :
    item = input('Enter anything: ')
    my_list.append(item)
    print(item)
    print(my_list)
    number -= 1
print('List complete')
