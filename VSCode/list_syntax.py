chars = list("Hello")
print(chars)
print(len(chars))

# initializing default values of list with iterable
values = list(range(0, 11, 2))
print(values)
print(len(values))

# two list are combined using +
combined = chars + values
print(combined)

# list initialization with repetition
repeat = [1, 2, 3] * 3
print(repeat)

# list of lists
multi_list = [[1, 2], [3, 4]]
print(multi_list)
