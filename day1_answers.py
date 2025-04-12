#1.Python program for Hello World
'''
print("Hello world")
'''

#2.Python program to add Two Numbers
'''
a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
print(a+b)
'''

#3.Python program to subtract two numbers
'''
a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
print(a-b)
'''

#4.Python Program to Multiply Two numbers
'''
a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
print(a*b)
'''

#5.Python program for Arithmetic Operations
'''
a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
print("Addition :- ",a+b)
print("Subtraction :- ",a-b)
print("Multiplication :- ",a*b)
print("Division :- ",a/b)
print("Floor :- ",a//b)
print("Modulus :- ",a%b)
print("Exponent :- ",a**b)
'''

#6.Python program to print Calendar
'''
import calendar

year = int(input("Enter year :-"))
month = int(input("Enter Month :- "))
res = calendar.month(year,month)
print(res)
'''

#7.Python program to find Largest of 2 Numbers
'''
n1 = int(input("ENter first number :- "))
n2 = int(input("Enter second number :- "))
if(n1>n2):
    print(n1," is greater")
else:
    print(n2," is greater")
'''

#8.Python program to find Largest of 3 Numbers
'''
n1 = int(input("ENter first number :- "))
n2 = int(input("Enter second number :- "))
n3 = int(input("Enter third number :- "))
if(n1>n2 and n1>n3):
    print(n1," is greater than ",n2," and ",n3)
elif(n2>n3):
    print(n2," is greater than ",n1," and ",n3)
else:
    print(n3," is greater than ",n2," and ",n1)
'''

#9.Python program for Leap Year
'''
year = int(input("Enter any month :- "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a leap year")
        else:
            print("Not a leap year")
    else:
        print("leap")
else:
    print("Not leap")
'''

#10.Python Program to Print Negative Numbers in a Range
'''
start = int(input("Enter start"))
end = int(input("Enter end"))
for i in range(start,end+1,1):
    print(i)
'''

#11.Python Program to Print Positive Numbers in a Range
'''
start = int(input("Enter start"))
end = int(input("Enter end"))
for i in range(start,end+1):
    print(i)
'''

#12.Python program to find Positive or Negative
'''
num = int(input("Enter any number :- "))
if(num < 0):
    print("Negative")
elif(num > 0):
    print("Positive")
'''

#13.Python program to check Number Divisible by 5 and 11
'''
num = int(input("Enter any number :- "))
if(num%5 == 0 and num %11 == 0):
    print("Num is divisible by both 5 and 11")
elif(num % 5 == 0):
    print("Num is divisible by 5")
elif(num % 11 == 0):
    print("Num is divisible by 11")
'''

#14.Python Program to Find the Sum and Average Of Three Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
num3 = int(input("Enter third number :- "))
total = num1+num2+num3
print(total)
avg = total / 3
print(avg)
'''

#15.Python Program to Find the Average Of Two Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
total = num1+num2
avg = total / 2
print(avg)
'''

#16.Python Program to Get Current Date and Time
'''
from datetime import datetime
print(datetime.today())
'''
