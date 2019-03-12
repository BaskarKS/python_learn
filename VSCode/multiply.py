def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start Debugging")
result = multiply(2, 3, 4)
print(result)
