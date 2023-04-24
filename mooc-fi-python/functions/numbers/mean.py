# create a function that takes three arguments and prints out the mean

def mean(num1, num2, num3) :
    total = float(num1 + num2 + num3)
    return float(total / 3)


if __name__ == '__main__' :
    print(f'The mean of your numbers is: {mean(4.6, 10.4, 12)}')