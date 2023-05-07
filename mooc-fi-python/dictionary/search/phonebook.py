"""
    Program: simple phone book that stores data
    keys: can be added and search. They are the contact name
    values: phone numbers stored using the keys
    
"""
phone_book = {}

for i in range(5) : # to control the loop for testing
    user_query = input('Enter 1 to search, 2 to add a contact or 3 to quit: ')
    if user_query == '1' :
        search = input('Enter the name you are looking for: ')
        if search in phone_book :
            print(f'name: {search}')
            print(f'number: {phone_book[search]}')
        elif search not in phone_book :
            print('Contact not found')
            continue
    elif user_query == '2' :
        add_contact = input('Enter a contact to be added to the phone book: ')
        add_number = input('Enter a number to be added to the contact: ')
        phone_book[add_contact] = add_number
        print(f'Name: {add_contact}')
        print(f'Number: {phone_book[add_contact]}')
        print('Contact added') 
    elif user_query == '3' :
        print('quitting...')
        break
    print(phone_book)     