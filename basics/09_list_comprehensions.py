# List comprehensions

# Basic list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# List comprehension with if statement
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# List comprehension with if-else statement
odds_and_evens = [x if x % 2 == 0 else -x for x in range(10)]
print(odds_and_evens)

# Nested list comprehension
nested_list = [[x for x in range(3)] for y in range(3)]
print(nested_list)
