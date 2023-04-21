# uses hashes to print rows and columns from user input

rows = int(input('Enter a number: '))
columns = int(input('Enter another number: '))
line = '#'*rows

while columns > 0 :
    print(line)
    columns -= 1
    