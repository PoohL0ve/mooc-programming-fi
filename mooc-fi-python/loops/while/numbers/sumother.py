limit = int(input('Enter a limit: '))
number = 1
total = 0

print(f'Limit: {limit}') 
while total < limit :
    total = total + number
    number += 1
print(total)
