# operand = int(input('Operand:'))
# operation = input("Choose an operation (+, -, *, /):")
# operator = int(input('Operator:'))

# result = 0

# if operation == "+":
#     result = operation + operand
# elif operation == "-":
#     result = operation - operand
# elif operation == "*":
#     result = operation - operand
# elif operation == "/":
#     result = operation - operand
# else:
#     print("Error: Invalid operation.")
# print(result)



# try:
#     operand = int(input('Operand:'))
#     operation = input("Choose an operation (+, -, *, /):")
#     operator = int(input('Operator:'))
    
#     result = 0
    
#     if operation == "+":
#         result = operation + operand
#     elif operation == "-":
#         result = operation - operand
#     elif operation == "*":
#         result = operation - operand
#     elif operation == "/":
#         result = operation - operand
#     else:
#         print("Error: Invalid operation.")
# except:
#     print("Error: Invalid number.")


# print("While Loops")
# print("===============")
# print("===============")
# print("===============")


# n = 1 

# while n < 5:
#     print('Hello pythonista')
#     n = n+1


# n = 1

# while n < 5:
#     print('Hello pythonista')
#     n = n+2
#     if n == 4:
#         break


# n = 1

# while n < 5:
#     if n  == 2:
#         n = n+1
#         continue
#     print('Hello pythonista')
#     n = n+1


# z = 0

# while z < 3:
#     if z == 0:
#         print("z is",z)
#         z += 1
#     elif z == 1:
#         print("z is",z)
#         z += 1
#     else:
#         print("z is",z)
#         z += 1


# myList = []
# i = 0

# while len(myList) < 4 :
#     myList.append(i)
#     i += 1
  
# print(myList)


# n = 10

# while n <= 100:
#     print(n ,end = ",")
#     n = n+10

# myTuple = (10,20,30,40,50,60)
# i = 0

# while i < len(myTuple):
#     print(myTuple[i])
#     i += 1

# myList = [23,45,12,10,25]
# i = 0 
# sum = 0

# while i < len(myList):
#     sum += myList[i]
#     i += 1

# print(sum)

# fruitsList = ["Mango","Apple","Orange","Guava"]

# while fruitsList:
#     print(fruitsList.pop())

# print(fruitsList)

# i = 0 
# word = "Hello"


# while i < len(word):
#     if word[i] == "e" or word[i] =="o":
#         i += 1
#         continue

#     print("Returned letter",word[i])
#     i += 1

# n = int(input("Enter a number: "))

# while n != 0:
#     n = int(input("Enter zero to quit: "))

# num = int(input("Enter a number: "))
# b = 0
# p = 1
# n = num

# while n>0:
#     rem = n%2
#     b += rem * p
#     p = p*10
#     n = n//2

# print("Binary value: ",b)

# p = 5
# sum = 0
# count = 0

# while p > 0:
#     count += 1
#     f = int(input("Enter the number "))
#     sum += f
#     p -= 1
  
# average = sum/count
# print("Average of given Numbers:",average)

# n = 1

# while n <= 5:
#     squareNum = n**2
#     print(n,squareNum)
#     n += 1

# n = int(input("Enter an integer: "))

# i = 1
# while i <= 10:
#     mul = i*n
#     i += 1
#     print(mul)

# n = int(input("Enter a number: "))
# rev = 0

# while n!=0:
#     r = n%10
#     rev = rev * 10 + r
#     n = n//10
    
# print("Reversed number:",rev)


# i = 0
# sum = 0
# n = int(input("Enter the number n: "))

# while  i <= n:
#     if i % 2 == 0:
#         sum += i
#     i += 1
        
# print("Sum of even numbers till n:",sum)

# n = int(input("Enter the number: "))
# f =n
# r = 1

# while f != 0 :
#     r *= f 
#     f -= 1
# print("Factorial of",n,"is:",r)




# print("For Loops")
# print("===============")
# print("===============")
# print("===============")

# for i in "pythonista":
#     print(i)


# for j in range(5):
#     print(j)



# AnimalList = ['Cat', 'Dog', 'Tiger', 'Cow']
# for x in AnimalList:
    
#     print(x)

# programmingLanguages = {'J':'Java','P':'Python'}

# for key in programmingLanguages.keys():
#     print(key,programmingLanguages[key])


# programmingLanguages = {'J':'Java','P':'Python'}
# for key,value in programmingLanguages.items():
#     print(key,value)


# a1 = ['Python','Java','CSharp']
# b2 = [1,2,3]

# for i,j in zip(a1,b2):
#     print(i,j)


# flowers = ['Jasmine','Lotus','Rose','Sunflower']
# for f in flowers:
#     print(f)
# else:
#     print('Done')

# list1 = [5,10,15,20]
# list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

# for x in list1:
#     for y in list2:
#         print(x,y)

# vehicles = ['Car','Cycle','Bus','Tempo']

# for v in vehicles:
#     if v == "Bus":
#         break
#     print(v)


# vehicles = ['Car','Cycle','Bus','Tempo']

# for v in vehicles:
#     if v == "Bus":
#         continue
#     print(v)

# numbers = [12,3,56,67,89,90, 10]
# count = 0

# for n in numbers:
#     count += 1

# print(count)

# numbers = [12,3,56,67,89,90]
# sum = 0

# for n in numbers:
#     sum += n

# print(sum)

# numbers = [2,5,6,10,15,20,25,30,33,35]

# for n in numbers:
#     if n%2 == 0:
#         print(n)

# for i in range(1,5):
#     for j in range(i):
#         print('H',end='')
#     print()

# list1 = ['Mango','Banana','Orange']
# list2 = []
# for i in list1:
#     list2.append(i)
    
# print(list2)

# numbers = [1,4,100,80,12]
# max = 0

# for n in numbers:
#     if(n>max):
#         max = n
        
# print(max)

# numbers = [1,4,50,80,12]
# min = 1000

# for n in numbers:
#     if(n<min):
#         min = n

# print(min)

# numbers = [1,4,50,80,12]

# for i in range(0, len(numbers)):    
#     for j in range(i+1, len(numbers)):    
#         if(numbers[i] > numbers[j]):    
#             temp = numbers[i]   
#             numbers[i] = numbers[j];    
#             numbers[j] = temp 

# print(numbers)

# numbers = [1,4,50,80,12]

# for i in range(0, len(numbers)):    
#     for j in range(i+1, len(numbers)):    
#         if(numbers[i] < numbers[j]):    
#             temp = numbers[i]   
#             numbers[i] = numbers[j];    
#             numbers[j] = temp 

# print(numbers)


# for i in range(3,20,2):
#   print(i)

# for i in range(5,20,5):
#   print(i)

# for i in range(10,0,-1):
#   print(i)