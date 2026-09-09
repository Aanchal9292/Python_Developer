# Q1 Print numbers 1 to 10
# for i in range(1,11):
#     print(i)

# Q2 Print even numbers 1 to 50
# for i in range(1,51):
#     if i%2==0 :
#         print(i)
# ----------------or------------------
# for i in range(2, 51, 2):
#     print(i)

# Q3 Print odd numbers 1 to 50
# for i in range(1,51):
#     if i%2!=0 :
#         print(i)



# Q4 Print multiplication table of a number
num = int(input("Enter the number : "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")