fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()

weekday = {}



for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        keys = line.split()
        if len(keys) > 2:
            mails = keys[1]
            weekday[keys[1]] = weekday.get(keys[1], 0) + 1
        
max_email = ''
max_number = 0
for key in weekday:
    if weekday[key] >= max_number:
        max_number = weekday[key]
        max_email = key
        
print(max_email, max_number)