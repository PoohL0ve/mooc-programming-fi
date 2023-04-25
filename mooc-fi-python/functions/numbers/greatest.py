# create a function that takes three arguments and return the largest number

def greatest(num1, num2, num3) :
    if num1 > num2 and num1 > num3 :
        return num1
    elif num2 > num1 and num2 > num3 :
        return num2
    else :
        return num3
    
#test for the largest number
if __name__ == '__main__' :
    print(greatest(4, 7, 5))