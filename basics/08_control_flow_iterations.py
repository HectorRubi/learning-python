# For Statement
for i in range(5):
    print(i)

# For Statement with else
for i in range(5):
    print(i)
else:
    print("Loop finished")


# While Statement
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")


# While Statement with break
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Loop finished")

# While Statement with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("Loop finished")
    print("a is equal to b")


# For Statement with break
for i in range(5):
    if i == 3:
        break
    print(i)
else: 
    print("Loop finished")
    print("a is equal to b")

# For Statement with continue
for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("Loop finished")
    print("a is equal to b")

