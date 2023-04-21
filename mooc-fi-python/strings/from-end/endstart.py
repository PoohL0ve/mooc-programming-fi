# print the input string from end to the start

word = input('Enter a string: ')

neglength = len(word) - 1




while neglength >= 0 :
    backward = word[neglength]
    print(backward)
    neglength -= 1