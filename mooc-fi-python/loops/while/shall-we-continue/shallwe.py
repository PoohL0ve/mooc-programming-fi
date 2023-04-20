# if 'no' is inputted by the user, end the program

while True :
    greeting = print('hi')
    you_said = input('Shall we contine: ')
    if you_said == 'no' :
        break
print('okay then')