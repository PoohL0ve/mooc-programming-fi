# print the following leap year
leap_year = 0
while True :
    this_year = int(input('Enter the year: '))

    if this_year % 3 == 0 :
        leap_year = this_year + 1
        break
    print('Year: ', this_year)
    print('The next leap year is: ', leap_year)

    if this_year % 2 == 0 :
        leap_year = this_year + 4
        break
    print('Year: ', this_year)
    print('The next leap year is ', leap_year)
print('Yay, your calender is updated')
