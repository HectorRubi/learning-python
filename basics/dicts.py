# Basics of dictionaries in Python

# A dictionary is a collection of key-value pairs
# It is unordered, mutable, and indexed
# It is defined using curly braces {}
# Each key-value pair is separated by a colon (:)
# Each key-value pair is separated by a comma (,)

# Example of a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values in a dictionary
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30

# Adding a new key-value pair to the dictionary
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Updating a value in the dictionary
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair from the dictionary
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

# Looping through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 31
# job: Engineer

# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary

# Getting the length of the dictionary
print(len(my_dict))  # Output: 3

# Copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}
print(my_dict_copy)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

# Keys method
print(my_dict_copy.keys())  # Output: dict_keys(['name', 'age', 'job'])

# Values method
print(my_dict_copy.values())  # Output: dict_values(['John', 31, 'Engineer'])

# Items method
print(my_dict_copy.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('job', 'Engineer')])

# Nesting dictionaries
nested_dict = {
    "person": {
        "name": "Alice",
        "age": 25
    },
    "job": {
        "title": "Data Scientist",
        "company": "Tech Corp"
    }
}
print(nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 25}, 'job': {'title': 'Data Scientist', 'company': 'Tech Corp'}}
print(nested_dict["person"]["name"])  # Output: Alice
print(nested_dict["job"]["title"])  # Output: Data Scientist
