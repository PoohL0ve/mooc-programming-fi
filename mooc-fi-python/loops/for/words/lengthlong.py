# create a function that returns the length of the longest string in a list

def length_of_longest(words : list) :
    longest = 0
    for word in words : 
        my_word = word
        #print(my_word)
        length = len(my_word)
        #print(length)
        if length > longest :
            longest = length
    return(longest) # focus on indentation

# test for code
my_list = ['Usher', 'Adele', 'James', 'Harry', 'Beyonce']
print(length_of_longest(my_list))
