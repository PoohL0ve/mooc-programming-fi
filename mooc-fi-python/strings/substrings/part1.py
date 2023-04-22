# print the characters of the substring from 0 to the last in order

word = str(input('Please enter a word: '))
word_index = 0

while word_index <= len(word):
    print(word[:word_index])
    word_index += 1