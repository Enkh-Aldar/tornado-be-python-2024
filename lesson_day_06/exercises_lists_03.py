fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    delimeter = ','
    words = line.split(delimeter)
    print(words[0])