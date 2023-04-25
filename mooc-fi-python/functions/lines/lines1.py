# print a line based on two arguments
# the first is the length of the line and the second the string
# use only the first character in the line first character in the string
# if the second argument is an empty string, the line should be stars

def line(number, word) :
    if word != "" :
        print(word[0]*number)
    if word == "" :
        print('*'*number)   

# test for function:
if __name__ == '__main__' :
    line(5, 'this') 
        