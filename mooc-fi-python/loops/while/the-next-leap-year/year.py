# print the following leap year
this_year = int(input('Enter a year: '))
leap_year = 0
while True :
   if this_year % 4 == 0 and this_year % 100 != 0 :
    leap_year = this_year + 4 
    break
   
   if this_year % 4 == 1 :
    leap_year = this_year + 3
    break
   
   if this_year % 4 == 2 :
    leap_year = this_year + 2
    break
   
   if this_year % 4 == 3 :
    leap_year = this_year + 1
    break
   
print('The next leap year is: ', leap_year) 
