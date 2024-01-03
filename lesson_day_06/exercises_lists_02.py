unique_words = []
fhand = open('romeo.txt')
for el in fhand:
    f = el.split()
    for t in f:
        if t not in unique_words:
            unique_words.append(t)
unique_words.sort()
print(unique_words)