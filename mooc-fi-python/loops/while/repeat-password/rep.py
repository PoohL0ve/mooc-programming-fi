# program that validates a password

while True :
    password = input('Please enter a password: ')
    password_repeat = input('Please repeate the password: ')

    if password != password_repeat :
        print('Password do not match')
    if password == password_repeat :
        break
print('user account created')