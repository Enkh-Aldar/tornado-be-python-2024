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
        print(keys[1])
        weekday[keys[1]] = weekday.get(keys[1], 0) + 1
        max_values = (weekday[keys[1]])
        print(max_values)

        
print(weekday)
