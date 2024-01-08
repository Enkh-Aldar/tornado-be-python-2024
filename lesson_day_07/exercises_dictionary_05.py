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
        addr = keys[1]
        uname, domain = addr.split('@')
        print(domain)
        # print(uname)
        weekday[domain] = weekday.get(domain, 0) + 1
        # weekday[uname] = weekday.get(uname, 0) + 1
        
print(weekday)