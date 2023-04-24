# create a function that takes both a string and an integer
# print the string as many times as the integer specifies

love = 'Love should be the only thing we fight for'
number = 5

def print_many_times(text, times) :
    while times > 0 :
        print(text)
        times -= 1

print_many_times(love, number)