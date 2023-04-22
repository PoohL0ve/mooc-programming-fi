# print substring in reverse

word = str(input('Please enter a word: '))
word_index = len(word)

while word_index >= 0 :
    print(word[word_index:]) 
    word_index -= 1