import re
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()


count = 0

# for line in fhand:
#     line = line.rstrip()
#     word = re.findall('^Author', line)
#     count += 1
#     print('mbox-short.txt had', count, 'lines that matched ^Author')
word = input('Enter a regular expression: ')

for line in fhand:
    line = line.rstrip()
    
    if re.search(word, line):
        count += 1
        print('mbox.txt had', count, 'lines that matched', word)