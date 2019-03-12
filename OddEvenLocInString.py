#print even index values and odd index values on the entered string
str=input("Enter a String  to print its odd and even characters : ")
evenrange=range(0,len(str),2)
oddrange=range(1,len(str),2)
evenchars = ""
oddchars = ""

for index in evenrange:
	evenchars += str[index]

for index in oddrange:
	oddchars += str[index]
print(evenchars)
print(oddchars)