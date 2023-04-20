# updated version of sumother
# show the calculations performed
limit = int(input('Enter a limit: '))
number = 1
total = 0
count = ''

print(f'Limit: {limit}')

while total < limit :
    total = total + number
    count += f' {number} +'
    number += 1
print(f'the consecutive sum is: {count} = {total} ')