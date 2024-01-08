import string
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()
    
    
alphabet = {}

for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    # print(words)
    for char in words:
        alphabet[char] = alphabet.get(char, 0) + 1
    print(alphabet)
    
lst = list()
for key, val in list(alphabet.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
