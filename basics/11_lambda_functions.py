# Lambda functions
add = lambda a, b: a + b
result = add(3, 5)
print(f"Sum: {result}")

# Lambda function with default argument
greed = lambda name="World": print(f"Hello, {name}!")
greed()

# Lambda function with return value
add = lambda a, b: a + b
result = add(3, 5)
print(f"Sum: {result}")

# Lambda function with multiple arguments
multiply = lambda a, b: a * b
result = multiply(3, 5)
print(f"Product: {result}")

# Lambda function with no arguments
no_arg = lambda: "No arguments here!"
result = no_arg()
print(result)

# Lambda function with conditional expression
conditional = lambda x: "Even" if x % 2 == 0 else "Odd"
result = conditional(4)
print(f"4 is {result}")

# Lambda function with list comprehension
squared = lambda x: [i ** 2 for i in x]
result = squared([1, 2, 3, 4])
print(f"Squared: {result}")

# Lambda function with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared with map: {squared}")

# Lambda function with filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
