# user decides if to add an item to the list or not
# to exit the loop, type x

my_list = []
item = 0

while True :
    choice = input('Enter (a) to add an item, (r) to remove an item or (x) to quit: ')

    if choice == 'a' :
        item += 1
        my_list.append(item)
        print(my_list)
    if choice == 'r' :
        my_list.pop(-1)
        print(my_list)
    if choice == 'x' :
        break
print('The fun is over')
