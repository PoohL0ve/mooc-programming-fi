# create a function to return the shortest string in a list

def shortest(words : list) :
    smallest = words[0]
    #print(smallest)
    for i in words :
        if len(i) < len(smallest):
            #print(len(i), len(smallest))
            smallest = i
    print(smallest)

# test for code
my_words = ['see', 'hear', 'U']
shortest(my_words)