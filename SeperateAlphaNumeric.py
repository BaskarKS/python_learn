#input is M8B9C8H4 and output is BCHM and 4889
str=input("Enter a String  sequence in combine of alpha numeric : ")
alphabet = ""
numeric = ""
for char in str:
	if char.isalpha():
		alphabet+= char
	elif char.isnumeric():
		numeric += char

print(alphabet)
print(numeric)
list = sorted(alphabet)
sortedstr = "".join(list)
print(sortedstr)
print("".join(sorted(numeric)))
