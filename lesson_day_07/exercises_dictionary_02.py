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
        print(keys[2])
        weekday[keys[2]] = weekday.get(keys[2], 0) + 1
        myKeys = list(weekday.keys())
        myKeys.sort()
        sorted_dict = {i : weekday[i] for i in myKeys}
        print(sorted_dict)

print(weekday)