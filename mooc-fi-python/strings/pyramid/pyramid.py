# pyramid of 10 rows
rows = 10
display = '#'

while rows > 0 : 
    print('' * rows + display)
    display += '##'
    rows -= 1
    