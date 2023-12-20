# inp = input('Enter Fahrenheit Temperature:')
# fahr = float(inp)
# calcius = (fahr - 32.0) * 5.0 / 9.0
# print(calcius)

inp = input('Enter Fahrenheit Temperature:')
try:
    fahrenheit = float(inp)
    celcius = (fahrenheit - 32.0) * 5.0 / 9.0 
    print(celcius)
except:
    print('Please enter a number')