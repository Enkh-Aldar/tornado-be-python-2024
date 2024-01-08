fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()
    
timeofday = dict()



for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        # print(line[5])
        addr = line[5]
        time = addr.split(':')
        # print(time)
        timeofday[time[0]] = timeofday.get(time[0], 0) + 1

lst = list()
for val, key in list(timeofday.items()):
    lst.append((val, key))

lst.sort()

for val, key in lst:
    print(val, key)
    
# print(timeofday)