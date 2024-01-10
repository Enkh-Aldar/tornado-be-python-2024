import re
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
lst = list()

for line in fhand:
    line = line.rstrip()
    numbers = re.findall('^New Revision:(\s[0-9.]+)', line)
    # print(numbers)
    if len(numbers) > 0:
        for number in numbers:
            number = int(number)
        lst.append(number)

avg = sum(lst)//len(lst)
print(avg)