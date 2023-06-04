"""
    The function smallest_average accepts 3 dictionaries as arguments:
    my_test[] : turns a dictionary into an object
    test : extracts the number values
    check : changes strings to integers
    my_sum : finds the total of the integers
    average : uses the figure 3 to find the mean
    return : returns the dictionary that has the smallest average
"""

def smallest_average(person1: dict, person2: dict, person3: dict) :
    my_test1 = []
    my_test2 = []
    my_test3 = []
    my_sum1 = 0
    my_sum2 = 0
    my_sum3 = 0
    average1 = 0
    average2 = 0
    average3 = 0
    # change dict to list
    for value in person1.values() :
        if not value in my_test1 :
            my_test1.append(value)
    test1 = my_test1[1:4]
    
    for value in person2.values() :
        if not value in my_test2 :
            my_test2.append(value)
    test2 = my_test2[1:4]
    
    for value in person3.values() :
        if not value in my_test3 :
            my_test3.append(value)
    test3 = my_test3[1:4]
    
    # extracting the number and finding the total
    
    for number in test1 :
        check = int(number)
        my_sum1 += check
    average1 = my_sum1 / 3
    
    for number in test2 :
        check2 = int(number)
        my_sum2 += check2
    average2 = my_sum2 / 3
    
    for number in test3 :
        check3 = int(number)
        my_sum3 += check3
    average3 = my_sum3 / 3
    
    # finding the smallest
    if average1 < average2 and average1 < average3 :
        return person1
    elif average2 < average1 and average2 < average3:
        return person2
    elif average3 < average1 and average3 < average2 :
        return person3
# test for function
if __name__ == "__main__" :
    ben = {"name": "Ben", "result1": 6, "result2": 3, "result3": 8}
    arie = {"name": "Arie", "result1": 4, "result2": 7, "result3": 5}
    ted = {"name": "Ted", "result1": 9, "result2": 2, "result3": 8}
    print(smallest_average(ben, arie, ted))
