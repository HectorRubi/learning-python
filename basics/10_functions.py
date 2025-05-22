# Functions
def greet(name):
    """Function to greet a person."""
    print(f"Hello, {name}!")
# Function call
greet("Alice")

# Function with default argument
def greet(name="World"):
    """Function to greet a person with a default name."""
    print(f"Hello, {name}!")
greet()

# Function with return value
def add(a, b):
    """Function to add two numbers."""
    return a + b
result = add(3, 5)
print(f"Sum: {result}")