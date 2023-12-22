# def f(x, y):
#     added = (x * x) + (y * y)
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


def convert_temperature():
    try:
        grad = input('Grad:')
        temperature = int(input('Temperature:'))
    
        if grad == "C":
            result = temperature * (9/5) + 32
        elif temperature == "C":
            result = (temperature - 32) * 5/9
    except:
        print("Error")
            
    print(result)
            
convert_temperature()

    
