# print('===========================')
# print('Lesson Day 04 ~ Exercises 1')
# print('===========================')

# n = 15 
# i = 25
# sum = 0

# while n <= i:
#     sum += n
#     n = n + 1
    
# print(sum)
    
# print('===========================')
# print('Lesson Day 04 ~ Exercises 2')
# print('===========================')

# n = 0 

# while n < 10:
#     print('Hello World')
#     n = n+1
    
    
# print('===========================')
# print('Lesson Day 04 ~ Exercises 3')
# print('===========================')

# count = 1
# i = 10
# multi = 1


# while count < i:
#     multi *= count
#     count = count + 1

# print(multi)


# print('===========================')
# print('Lesson Day 04 ~ Exercises 4')
# print('===========================')

# def convert_to_binary():
#     num = int(input("Enter a number: "))
#     binary = 0
#     p = 1

#     while num > 0:
#         rem = num % 2
#         num = num // 2
#         binary += rem * p
#         p = p * 10

#     print("Binary value: ",binary)
# convert_to_binary()




# print('===========================')
# print('Lesson Day 04 ~ Exercises 5')
# print('===========================')

# def convert_to_decimal():
#     num = int(input("Enter a number: "))
#     decimal = 0
#     p = 1

#     while num != 0:
#         rem = num % 10
#         decimal = decimal + rem * p
#         p = p * 2
#         num = num // 10

#     print("Decimal value: ", decimal)
    
# convert_to_decimal()


# print('===========================')
# print('Lesson Day 04 ~ Exercises 5')
# print('===========================')

# def convert_to_decimal():
#     decimal = int(input("Enter a number: "))
#     rest = 0
#     power = 0

#     while decimal > 0:
#         if decimal % 10 ** (power + 1) != 0:
#             rest = rest + 2**power
#             decimal = decimal - 10**power
#         power += 1

#     print("Decimal value: ", rest)
    
# convert_to_decimal()


print('===========================')
print('Lesson Day 04 ~ Exercises 5')
print('===========================')

def convert_to_decimal(n):
    n = str(n)
    n = n[::-1]
    decimal = 0

    for bin, digit in enumerate(n):
        decimal += int(digit) * (2**bin)
    return decimal

num = input('Enter a number:')

print(convert_to_decimal(num))

# def convert_to_decimal():
#     num = int(input("Enter a number: "))
#     decimal = 0
#     p = 1

#     while num != 0:
#         rem = num % 10
#         decimal = decimal + rem * p
#         p = p * 2
#         num = num // 10

#     print("Decimal value: ", decimal)
    
# convert_to_decimal()

print('===========================')
print('Lesson Day 04 ~ Exercises 6')
print('===========================')

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)

    index = index + 1
