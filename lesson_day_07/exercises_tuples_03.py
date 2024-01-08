import string
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File Cannot be opened:', fname)
    exit()
    
file_list = fhand.read()
# print(file_list)

letters = 'abcdefghijklmnopqrstuvwxyz'

alphabet_dict = {letter: 0 for letter in letters}

# print(alphabet_dict)

for char in file_list.lower():
    if char in letters:
        alphabet_dict[char] += 1

    
total_num_letters = sum(alphabet_dict.values())

sorted_pairs = sorted([(value, key) for (key, value ) in alphabet_dict.items()], reverse=True)

# print(sorted_pairs)
    
for value, letter in sorted_pairs:
    percentage = 100 * value / total_num_letters
    print(f'{letter}: {value}\t({percentage:.2f}%)')