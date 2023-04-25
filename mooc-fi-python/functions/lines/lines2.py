# call a function inside a function to print specified lines

def line(number, word) :
    if word != "" :
        print(word[0]*number)
    if word == "" :
        print('*'*number)

if __name__ == '__main__' :
    number = 5
    word = 'this'
    line(number, word)
        
def rectangle(times) :
    while times > 0 :
        line(number, word)
        times -= 1 

# test for function rectangle()
if __name__ == '__main__' :
    rectangle(5)