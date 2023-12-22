operand = int(input('Operand:'))
operation = input("Choose an operation (+, -, *, /):")
operator = int(input('Operator:'))

result = 0

if operation == "+":
    result = operation + operand
elif operation == "-":
    result = operation - operand
elif operation == "*":
    result = operation - operand
elif operation == "/":
    result = operation - operand
else:
    print("Error: Invalid operation.")
print(result)



try:
    operand = int(input('Operand:'))
    operation = input("Choose an operation (+, -, *, /):")
    operator = int(input('Operator:'))
    
    result = 0
    
    if operation == "+":
        result = operation + operand
    elif operation == "-":
        result = operation - operand
    elif operation == "*":
        result = operation - operand
    elif operation == "/":
        result = operation - operand
    else:
        print("Error: Invalid operation.")
except:
    print("Error: Invalid number.")