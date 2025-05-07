# Comparison operators
# Comparison operators are used to compare two values. They return a boolean value (True or False).
# The comparison operators are:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# Example:
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Logical operators
# Logical operators are used to combine conditional statements. They return a boolean value (True or False).
# The logical operators are:
# and  Returns True if both statements are true
# or   Returns True if one of the statements is true
# not  Returns True if the statement is false
# Example:
x = 10
y = 20
z = 30

print(x < y and y < z)  # True
print(x < y or y > z)   # True
print(not(x < y))       # False

# Identity operators
# Identity operators are used to compare the memory locations of two objects. They return a boolean value (True or False).
# The identity operators are:
# is   Returns True if both variables are the same object
# is not Returns True if both variables are not the same object
# Example:
a = [1, 2, 3]
b = a
c = a[:]

print(a is b)      # True
print(a is c)      # False
print(a is not b)  # False
print(a is not c)  # True

# Membership operators
# Membership operators are used to test if a value is in a sequence (string, list, tuple, set, dictionary). They return a boolean value (True or False).
# The membership operators are:
# in     Returns True if a value is found in the sequence
# not in Returns True if a value is not found in the sequence
# Example:
a = [1, 2, 3, 4, 5]
b = 3
c = 6
print(b in a)      # True
print(c not in a)  # True

# Bitwise operators
# Bitwise operators are used to perform bit-level operations on integers. They return an integer value.
# The bitwise operators are:
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR
# ~   Bitwise NOT
# <<  Bitwise left shift
# >>  Bitwise right shift
# Example:
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # 0 (0000 in binary)
print(a | b)  # 14 (1110 in binary)
print(a ^ b)  # 14 (1110 in binary)
print(~a)     # -11 (inverts all bits)
print(a << 1)  # 20 (10100 in binary)
print(a >> 1)  # 5 (0101 in binary)

# Assignment operators
# Assignment operators are used to assign values to variables. They return the value assigned to the variable.
# The assignment operators are:
# =   Assigns a value to a variable
# +=  Adds a value to a variable and assigns the result to the variable
# -=  Subtracts a value from a variable and assigns the result to the variable
# *=  Multiplies a variable by a value and assigns the result to the variable
# /=  Divides a variable by a value and assigns the result to the variable
# %=  Modulus operator assigns the remainder of a division to the variable
# //= Divides a variable by a value and assigns the result to the variable (floor division)
# **= Raises a variable to the power of a value and assigns the result to the variable
# Example:
a = 10
b = 5
a += b  # a = a + b
print(a)  # 15
a -= b  # a = a - b
print(a)  # 10
a *= b  # a = a * b
print(a)  # 50
a /= b  # a = a / b
print(a)  # 10.0
a %= b  # a = a % b
print(a)  # 0.0
a //= b  # a = a // b
print(a)  # 0.0
a **= b  # a = a ** b
print(a)  # 0.0

# Ternary operator
# The ternary operator is a shorthand way of writing an if-else statement. It returns one of two values based on a condition.
# The syntax is:
# value_if_true if condition else value_if_false
# Example:
a = 10
b = 20
result = "a is greater" if a > b else "b is greater"
print(result)  # b is greater
# The ternary operator can also be used to assign a value to a variable based on a condition.
# Example:
a = 10
b = 20
result = a if a > b else b
print(result)  # 20
# The ternary operator can also be used to assign a value to a variable based on a condition.
# Example:
a = 10
b = 20
result = a if a > b else b
print(result)  # 20
# The ternary operator can also be used to assign a value to a variable based on a condition.
# Example:
a = 10
b = 20
result = a if a > b else b
print(result)  # 20
# The ternary operator can also be used to assign a value to a variable based on a condition.
# Example:
a = 10
b = 20
result = a if a > b else b