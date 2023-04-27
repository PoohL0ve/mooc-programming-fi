# create a function that takes one argument
# return true if the string is a palindrome
# palindrome are words that are the same when reversed: 'oddo'

def palindrome(word : str) :
    my_word = ''
    for letter in range(len(word), 0, -1) :
        my_word += word[letter - 1]
    if my_word == word :
        return 'This is a palindrome'
    else :
        return 'This is not a palindrome'
    
# test for function
guess = palindrome('deed')
print(guess)
