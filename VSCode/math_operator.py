import math
#number operators
x = 100
y = 20
val_one = 2
val_two = 5
print('Division result in float:', x / y)
print('Division result in int:', x // y)

print(f"Multiply {val_one} * {val_two}:", val_one * val_two)
print(f"Power value of {val_one} power {val_two} :", val_one**val_two)

rounding = 2.5
absolute = -3.5
print(f"rounding {rounding}: ", round(rounding))
print(f"ceil value {rounding}: ", math.ceil(rounding))
print(f"floor value {rounding}: ", math.floor(rounding))

print(f"absolute value of {absolute}: ", abs(absolute))
print(f"absolute value of {absolute}: ", round(abs(absolute)))
