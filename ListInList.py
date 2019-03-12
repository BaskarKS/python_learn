#list inside list, printing the list inside in list by row wise and matrix style
x= [[10,20,30], [40,50,60], [70,80,90]]
print(x)
print("Printing Row Wise : ")
for r in x:
	print(r)

print("Printing elements in Matrix Style : ")
for row in range(len(x)):
	for col in range(len(x[row])):
		print(x[row][col], end = ' ')
	print()	