# Generator function that returns even numbers

def even_numbers(beg: int, end:int) :
    for number in range(beg, end+1) :
        if number % 2 == 0 :
            yield number

numbers = even_numbers(11, 21)
for number in numbers :
    print(number)