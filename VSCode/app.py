# Handling different exceptions using with block multi resources
try:
    with open("app.py") as file1, open("test.py", "w") as file2:
        print(file1)
        print(type(file1))
        print(file2)
        print(type(file2))
        print("File opened for read and closed prop")
    age = int(input("Enter Age : "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError) as ex:
    print("exception type {} and value : {}".format(type(ex), ex))
    print("Enter valid age between 1-110")
else:
    print("will be printed if no exception occurs")
print("Exceution continues ....")
