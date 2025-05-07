# Lists in python are mutable, ordered collections of items.
# They can contain items of different data types, including other lists.
# Lists are defined using square brackets [].
# Lists are zero-indexed, meaning the first item has an index of 0.

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing list items
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2
print(my_list[-1])  # Output: 5 (last item)
print(my_list[-2])  # Output: 4 (second to last item)

# Slicing lists
# Slicing allows you to access a range of items in a list.
print(my_list[1:3])  # Output: [2, 3] (items from index 1 to 2)
print(my_list[:3])   # Output: [1, 2, 3] (items from start to index 2)
print(my_list[2:])   # Output: [3, 4, 5] (items from index 2 to end)
print(my_list[:])    # Output: [1, 2, 3, 4, 5] (all items)
print(my_list[::2])  # Output: [1, 3, 5] (every second item)
print(my_list[::-1])  # Output: [5, 4, 3, 2, 1] (reversed list)

# Modifying lists
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)  # Output: [10, 20, 30, 4, 5]
my_list[1:3] = [25]
print(my_list)  # Output: [10, 25, 4, 5]
my_list[1:3] = []
print(my_list)  # Output: [10, 5]
my_list[1:1] = [15, 20]
print(my_list)  # Output: [10, 15, 20, 5]


# Adding items to a list

# Adds 30 to the end of the list
my_list.append(30) 
print(my_list)  # Output: [10, 15, 20, 5, 30]

# Inserts 25 at index 2
my_list.insert(2, 25)
print(my_list)  # Output: [10, 15, 25, 20, 5, 30]

# Extends the list with multiple items
my_list.extend([35, 40])
print(my_list)  # Output: [10, 15, 25, 20, 5, 30, 35, 40]


# Removing items from a list

# Removes the first occurrence of 20
my_list.remove(20)
print(my_list)  # Output: [10, 15, 25, 5, 30, 35, 40]

# Removes the item at index 3 (5)
del my_list[3]
print(my_list)  # Output: [10, 15, 25, 30, 35, 40]

# Removes the last item and returns it
last_item = my_list.pop()
print(last_item)  # Output: 40
print(my_list)  # Output: [10, 15, 25, 30, 35]

# Removes all items from the list
my_list.clear()
print(my_list)  # Output: []


# Max and Min
# Find the maximum and minimum values in a list
my_list = [10, 15, 25, 5, 30, 35]
print(max(my_list))  # Output: 35
print(min(my_list))  # Output: 5

# List comprehension

# List comprehension is a concise way to create lists.
# It consists of an expression followed by a for clause and zero or more for or if clauses.
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension with a condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Nested lists
# Lists can contain other lists, creating a nested structure.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][2])  # Output: 6 (item at index 2 of the second list)
print(nested_list[2][0:2])  # Output: [7, 8] (items from index 0 to 1 of the third list)

# List methods
# Lists have several built-in methods for common operations.
# Some of the most commonly used methods are:
# - append(item): Adds an item to the end of the list.
# - extend(iterable): Extends the list by appending elements from an iterable.
# - insert(index, item): Inserts an item at a specified index.
# - remove(item): Removes the first occurrence of an item from the list.
# - pop(index): Removes and returns the item at the specified index (default is the last item).
# - clear(): Removes all items from the list.
# - index(item): Returns the index of the first occurrence of an item.
# - count(item): Returns the number of occurrences of an item in the list.
# - sort(): Sorts the items of the list in place (ascending order by default).
# - reverse(): Reverses the order of the items in the list in place.
# - copy(): Returns a shallow copy of the list.
# - join(): Joins the elements of a list into a single string, using a specified separator.
# - split(): Splits a string into a list of substrings based on a specified separator.
# - find(): Returns the index of the first occurrence of a substring in a string.
# - replace(): Replaces all occurrences of a substring with another substring in a string.
# - format(): Formats a string using placeholders and values.
# - strip(): Removes leading and trailing whitespace from a string.
# - title(): Converts the first character of each word to uppercase and the rest to lowercase.
# - upper(): Converts all characters in a string to uppercase.
# - lower(): Converts all characters in a string to lowercase.
# - capitalize(): Converts the first character of a string to uppercase and the rest to lowercase.