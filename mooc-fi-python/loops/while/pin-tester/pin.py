# program that keeps asking for a pin until the correct one is typed: 4321
# print the number of times the user tried

attempts = 0

while True :
    pin = input('Please enter the correct pin: ')
    attempts += 1

    if pin == '4321' :
        success = True
        break
    print('Password successful')
if attempts == 1 :
    print('PIN: ',pin, 'Great! You Got it on one try')

# indentation is highly important
# remember where to place each line of code as whole loops can lose control