# def f(x, y):
#     added = x**2 + y**2
#     return added

# result = f(5, 6)

# print(result)

# def g(x,y):
#     a = (x * x) - 2 * y + (y * y)
#     return a

# result = g(7, 8)

# print(result)

# def t(x, y, z):
#     b = (x * x) + 3 * y * z + (y * y)
#     return b

# result = t(5, 6, 7)

# print(result)


# def convert_temperature():
#     try:
#         grad = input('Grad:')
#         temperature = int(input('Temperature:'))
    
#         if grad == "C":
#             result = temperature * (9/5) + 32
#         elif temperature == "C":
#             result = (temperature - 32) * 5/9
#     except:
#         print("Error")
            
#     print(result)
            
# convert_temperature()


def find_age(age):
    try:
        if (0 <= age) and (age <= 12):
            print('You are a Child')
        elif (age >= 13)and(age <= 19):
            print('You are Teenager')
        elif (age >= 20)and(age <= 59):
            print('You are a Adult')
        elif (age >= 60)and(age <= 100):
            print('You are a Senior')
        else:
            print('you are dinosaur')
    except:
        print('You Are Dinosaur')
        
find_age(101)
