# fill the right side of the line with * from the user input

word = str(input('Enter a word: '))
star = '*' #the line can only hold 20 characters
if len(word) > 0 and len(word) < 20 :
    remain_space = 20 - len(word)
    star = star*remain_space
    line = star + word
    print(line)
else :
    print('The word must have more than one character but less than 20')
    