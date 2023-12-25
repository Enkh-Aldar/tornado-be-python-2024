print('===========================')
print('Lesson Day 04 ~ Exercises 1')
print('===========================')

n = 15 
i = 25
sum = 0

while n <= i:
    sum += n
    n = n + 1
    
print(sum)
    
print('===========================')
print('Lesson Day 04 ~ Exercises 2')
print('===========================')

n = 0 

while n < 10:
    print('Hello World')
    n = n+1
    
    
print('===========================')
print('Lesson Day 04 ~ Exercises 3')
print('===========================')

count = 1
i = 10
multi = 1


while count < i:
    multi *= count
    count = count + 1

print(multi)


print('===========================')
print('Lesson Day 04 ~ Exercises 4')
print('===========================')


num = int(input("Enter a number: "))
binary = 0
p = 1

while num > 0:
    rem = num % 2
    binary += rem * p
    p = p * 10
    num = num //2

print("Binary value: ",binary)

print('===========================')
print('Lesson Day 04 ~ Exercises 5')
print('===========================')


num = int(input("Enter a number: "))
decimal = 0
p = 1

while num != 0:
    rem = num % 10
    decimal = decimal + (rem * p)
    p = p * 2
    num = int(num / 10)

print("Decimal value: ", decimal)