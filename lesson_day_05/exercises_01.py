print('python shout.py')
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From:'):
        print(line.upper())