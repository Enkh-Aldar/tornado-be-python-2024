
fname = input('Enter a file name: ')
fhand = open(fname)

count = 0
sum = 0
average = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        sum += float(line[-7:])
        average = sum / count 
print(average)