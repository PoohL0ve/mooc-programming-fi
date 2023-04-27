# create a function that takes two strings as arguments
# If the two strings are anagrams return True
# Use a for loop

def anagrams(word, saying) :
    organise = sorted(word)
    org_saying = sorted(saying)

    if organise == org_saying :
        return True
    else :
        return False
    
# Test for code
if __name__ == '__main__' :
    h2 = 'three'
    h3 = 'there'
    print(anagrams(h2, h3))