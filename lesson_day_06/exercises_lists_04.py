largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    if smallest == None or num < smallest:
        smallest = num
    if largest == None or num > largest:
        largest = num

print("Maximum: ", largest)
print("Minimum: ", smallest)