s=input("Enter a String to print characters and the length : ")
len=0
for x in s:
	print(type(x) , end=' => ')
	print(x)
	if (x is not ' '):
		len+=1
print("Length of the String : ", len)