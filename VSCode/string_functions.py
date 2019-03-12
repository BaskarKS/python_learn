#string functions
name = 'baskar kadari suribabu'
caps = name.upper()
print(caps)
print(caps.lower())
print(caps.title())

space_string = "   Jaasritha   "
print(space_string)

print(space_string.strip())
print(space_string.rstrip())
print(space_string.lstrip())

print(space_string.find('a'))
print(space_string.strip().find('a'))
print(space_string.replace('a', 'X'))
print(space_string.replace('a', 'X', 2))

print("aas" in space_string)
print("Jaa" not in space_string)
print("jaa" not in space_string)
