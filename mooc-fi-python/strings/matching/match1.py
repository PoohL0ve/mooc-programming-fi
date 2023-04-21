# if the second and second to last characters of a sting match print

word = input('Enter a word: ')

if word[1] == word[-2] :
    print('The second and the second to last characters are: ', word[1])
else :
    print('The second and second to last characters are different')