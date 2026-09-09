x = 5
y = "John"
print(x)
print(y)

# Casting 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# print type of variable
print(type(x))
print(type(y))
print(x)

# multiple values to multiple variables 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variable 
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpack values from list , tuple 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)