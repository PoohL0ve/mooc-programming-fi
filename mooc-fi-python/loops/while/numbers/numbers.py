# print integers more than zero but less than the input

number = int(input('Enter a number: '))
limit = 1

print('Upper Limit: ', number)

while limit > 0 and limit < number :
    print(limit)
    limit += 1
print('Done')