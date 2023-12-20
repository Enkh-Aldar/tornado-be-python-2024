print('Hello World')

a = 5

b = 6

string_type = 'Hello World'
print(string_type)


number_type = 5

print(number_type)

float_number_type = 5.5
print(float_number_type)

print(5 / 4)
print(4 * 4)
print(5 + 4)
print(5 - 4)
print(5 % 4)
print(5 ** 4)
print(5 // 4)
print((5 / 4) % 1)

name = input('Enter Your Name:')

print('Your name is ', name)

print(5 == 5)

x = 5
y = 6

print(x == y) 

print(x != y)

print(x > y)

print(x < y)

print(x >= y)

print(x <= y)

print(x is y)

print(x is not y)

print('===============')

print('===============')
age = 21

print((0 <= age) and (age <= 12))

print((age >= 13)and(age <= 19))

print((age >= 20)and(age <= 59))

print((age >= 60)and(age <= 100))

print('===============')
print('===============')

if x > 0:
    print('X is positive')
    
if (0 <= age) and (age <= 12):
    print('You are a Child')
elif (age >= 13)and(age <= 19):
    print('You are Teenager')
elif (age >= 20)and(age <= 59):
    print('You are a Adult')
elif (age >= 60)and(age <= 100):
    print('You are a Senior')
else:
    print('You Are Dinosaur')
    
c = int(input('Enter c:'))
d = int(input('Enter d:'))
if c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else:
    print('c is greather than d ')
    
if c == d:
    print('c is equal to d')
else:
    if c < d:
        print('c is less than d')
    else:
        print('c is greater than d')
        
if x < 0:
    if x < 10:
        print('x is a positive single digit number')