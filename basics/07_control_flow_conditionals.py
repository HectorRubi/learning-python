# Conditionals

# if statement
if True:
    print("This is true")

# if-else statement
if False:
    print("This is true")
else:
    print("This is false")

# if-elif-else statement
if False:
    print("This is true")
elif True:
    print("This is true")
else:
    print("This is false")


# Nested if statement
if True:
    print("This is true")
    if False:
        print("This is true")
    else:
        print("This is false")

# if statement with logical operators
if True and False:
    print("This is true")
elif True or False:
    print("This is true")
else:
    print("This is false")

# if statement with membership operators
a = [1, 2, 3]
if 1 in a:
    print("1 is in the list")
else:
    print("1 is not in the list")

# if statement with identity operators
a = [1, 2, 3]
b = a
if a is b:
    print("a is b")
else:
    print("a is not b")

# if statement with comparison operators
a = 1
b = 2
if a < b: 
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# if statement with ternary operator
a = 1
b = 2
c = a if a < b else b
print(c)  # Output: 1
