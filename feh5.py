try:
    with open('intro.txt', 'x') as f:
        f.write('New file created')
except FileExistsError:
    print('File already exists.')