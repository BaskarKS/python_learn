#input is a1b4m2n3 and output is abbbbmmnnn
str=input("Enter a String  sequence comb of alpha numeric : ")
output=""
for char in str:
	if char.isalpha():
		cache = char
	elif char.isnumeric():
		output += cache * int(char)
print(output)
