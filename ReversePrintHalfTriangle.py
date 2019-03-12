#print the entererd number of * in pyramid degrading
n=int(input("Enter the no of  decreasing size * print : "))
for i in range(n,0,-1):
	for j in range(1, i + 1):
		print("*", end=' ')
	print() 