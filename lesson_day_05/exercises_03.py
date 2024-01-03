fname = input("Enter a File name: ")


try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()



foutname = input('Enter a file name: ')
fouthand = open(foutname, 'w')

line1 = "NA NA NA BOO BOO TO YOU - You have been punk'd!\n"
fouthand.write(line1)
fouthand.close()


