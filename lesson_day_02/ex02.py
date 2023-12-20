hours = input('Enter Hours:')
rate = input('Enter Rate:')
try:
    rates = float(rate)
    print(rates)
except:
    print('Error, please enter numeric input')
    
try:
    hour = float(hours)
    print(hour)
except:
    print('Error, please enter numeric input')