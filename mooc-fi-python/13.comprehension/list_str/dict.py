"""
    The function takes a list of strings and returns a dictionary

    The dictionary uses keys for each word and values display the length of the word
"""

def lengths(strings: list) :
    check_dictionary = {character : len(character) for character in strings}
    return check_dictionary

# test for function
if __name__ == "__main__" :
    life = ["Sex", "Joy", "Beauty", "Challenge", "Pain"]
    print(lengths(life))
