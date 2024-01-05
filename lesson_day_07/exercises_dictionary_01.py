fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()

d1 = dict()
keys = []
d2 = {}
for line in fhand:
    key = line.split()
    for word in keys:
        d2[word] = d2.get(word, 0) +1
print(d2)  

