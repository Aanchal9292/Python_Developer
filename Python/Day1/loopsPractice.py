# Q1 Print numbers 1 to 10
# for i in range(1,11):
#     print(i)

# Q2 Print even numbers 1 to 50
# for i in range(1,51):
#     if i%2==0 :
#         print(i)
#     else :
#         continue

# Q3 Print odd numbers 1 to 50
# for i in range(1,51):
#     if i%2!=0 :
#         print(i)
#     else :
#         continue


# Q4 Print multiplication table of a number
# num = int(input("Enter the number : "))
# for i in range(1,11):
#     print(num*i)

# Q5 Sum of numbers from 1 to N
# num = int(input("Enter the number : "))
# sum = 0
# for i in range(1,num+1):
    
#     sum = sum + i
# print(f"Sum of first {num} is {sum}")


# Q6 Factorial of Number
# num = int(input("Enter the number : "))
# fact = 1
# if num < 0:
#     print("Factorial cannot be defined")
# else:
#     for i in range(1,num+1):
#         fact = fact*i
#     print("Factorial : ",fact)


# Q7 Reverse a Number
# num = int(input("Enter the number : "))
# rev = 0
# while num>0 :
#     rem = num%10
#     rev = rem + rev*10
#     num = num // 10
# print("Reversed Number : ",rev)


# Q8 Palindrome of a Number
o_num = num = int(input("Enter number : "))
rev = 0
while num>0 :
    rem = num %10 
    rev = rem + rev*10
    num = num// 10
if rev == o_num:
    print("Palindrome")
else :
    print("Not a palindrome")
