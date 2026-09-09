# Revision of python concepts from basics

# Q1  Check whether a number is positive, negative, or zero.
# num = int(input("Enter the number : "))
# if num<0 :
#     print(f"{num} is negative")
# elif num==0 :
#     print(f"{num} is zero")
# else :
#     print(f"{num} is positive")


# Q2  Find the largest of two numbers.
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1>num2 :
#     print(f"{num1} is greater")
# elif num2>num1 :
#     print(f"{num2} is greater")
# else :
#     print("Both are equal")

# Q3 Find the largest of three numbers.

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is greatest")

# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is greatest")

# else:
#     print(f"{num3} is greatest")

#Q4 Check whether a year is a leap year.
# year =  int(input("Enter the year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
#     print(f"{year} is leap year")
# else :
#     print(f"{year} is not a leap year")

# Q5 Create a simple calculator.
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# op = input("Enter operations (+,-,*,/,%) : ")
# if op=='+' :
#     print(f"Addition : {num1+num2}")
# elif op=='-' :
#     print(f"Subtraction : {num1-num2}")
# elif op=='*' :
#     print(f"Multiplication : {num1*num2}")
# elif op == '/':
#     if num2 != 0:
#         print(f"Division : {num1 / num2}")
#     else:
#         print("Cannot divide by zero")
# elif op=='%' :
#      print(f"Remainder : {num1%num2}")
# else :
#     print("Enter valid operand")


# Q6 Create a simple grade calculator.

marks = int(input("Enter the marks : "))
if marks<0 or marks >100 :
    print("Enter valid marks")
else :
    if  marks>=90 :
        print("Grade A+")
    elif marks>=80 :
        print("Grade A")
    elif marks>=70 :
        print("Grade B")
    elif marks>=60 :
        print("Grade C")
    elif marks>=40 :
        print("Grade D")
    else :
        print("Fail")

    