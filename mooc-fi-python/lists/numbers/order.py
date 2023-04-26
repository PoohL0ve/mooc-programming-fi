# print original and new sorted list from user input
# if 0 if entered, exit

original_list = []
while True :
    number = int(input("Enter a number greater than zero, or zero to exit: "))
    original_list.append(number)
    new_list = sorted(original_list)
    print(f'Original List: {original_list}')
    print(f'New List: {new_list}')

    if number == 0 :
        break