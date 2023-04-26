# use a function to return the mean of a list of integers

def mean(numbers : list) :
    total = sum(numbers)
    average = total // 2
    return average

# test for function
values = mean([34, 50, 77])
print(f'The mean of your list is {values}')
