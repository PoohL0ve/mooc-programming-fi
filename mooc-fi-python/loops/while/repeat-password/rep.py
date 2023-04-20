# program that validates a password

while True :
    password = input('Please enter a password: ')
    password_repeat = input('Please repeat the password: ')

    if password_repeat != password :
        print('Password do not match')
    if password_repeat == password :
        break
print('user account created')