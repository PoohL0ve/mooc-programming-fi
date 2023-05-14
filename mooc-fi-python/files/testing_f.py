# simple longer way to read the contents
test_file = open('testing.txt', 'rt')
print(test_file.read())
test_file.close()

# using the with statement to read, print and close
with open('testing.txt', 'rt') as this_file :
    check_file = this_file.read()
    print(check_file)