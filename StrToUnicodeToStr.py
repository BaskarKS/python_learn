#input is a3b2c5 and output is adbdch
str=input("Enter a String  sequence comb of alpha numeric : ")
output=""
for char in str:
	if char.isalpha():
		cache = char
		output+=cache
	elif char.isnumeric():
		output += chr(ord(cache)+int(char))
print(output)
