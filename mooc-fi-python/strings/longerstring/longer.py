# let user input 2 strings
# print the longer of the two

first_word = input('Enter a word or statement: ')
second_word = input('Enter another word or string: ')

if len(first_word) > len(second_word) :
    print(f'{first_word} is longer')
elif len(second_word) > len(first_word) :
    print(f'{second_word} is longer')
elif len(first_word) == len(second_word) :
    print(f'{first_word} and {second_word} are of equal length')