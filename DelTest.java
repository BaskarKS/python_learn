#use of del keyword of deleting a variable will impact otheer variable using the same object
s1=10
s2=10
s3=10
print(s1,s2,s3)
print(id(s1),id(s2),id(s3))
del s1
print(s2,s3)
print(id(s2),id(s3))