hours = int(input('Enter Hours:'))

rate = int(input('Enter Rate:'))

# # payment = 40 * rate + (hours - 40) * 1.5 * rate

# print(payment)

if hours <= 40:
    payment = hours * rate
else:
    payment = 40 * rate + (hours - 40) * 1.5 * rate
print(payment)