# underline the user's input
# stop the program when the user enters an empty string

while True :
    sentence = str(input('Enter a sentence: '))
    underline = '_'*len(sentence)
    if sentence == '' :
        break
    print(sentence)
    print(underline)