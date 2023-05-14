name = input('Who are you? ')
your_file = input('Enter a file for inscription: ')

with open(your_file, 'xt') as this_file :
    this_file.write(f'Hi, {name}, I hope you remain focused in achieving your goals and desires.')

with open(your_file, 'rt') as finished_file :
    print(finished_file.read())