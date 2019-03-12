#only boolean of below value will be false rest everything is true
print(bool(""))
print(bool(0))
print(bool(None))

print("*" * 15)
#bool value of everything is true
print(bool(-0.1))
print(bool(.1))

print(10 == '10')
print(ord('a'))
print(ord('z'))
print(ord('z') - ord('a'))
print(ord('9') - ord('1'))

#ssample of If conditional check
temperature = int(input("Enter current temperature : "))
if temperature > 30:
    print("its warm")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")

age = int(input("enter age : "))
if age >= 18:
    print("eligible")
else:
    print("not eligible")

#Ternery operator
message = "eligible" if age >= 18 else "not eligible"
value = age if age >= 18 else 0
print(message, f"{value}")

# variable = value1 condition else value2
#variable = condition ? value1 : value2
boolvalue = bool(input("enter True(success) | False(Failure):")
                 )  #only no input, just enter will return false
print(boolvalue)
decision = "sucess" if boolvalue else "failure"
print(decision)

#logical and,or,not and chaining of logical is short circuit operation
high_income = True
good_credit = False
student = False
if ((high_income or good_credit) and not student):
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

#relational operator check
age = 21
if age >= 18 and age <= 60:
    print("Eligible age to work")
else:
    print("Not eligible age to work")

#another way of using relation operator
if 18 <= age <= 60:
    print("Eligible age to work")
else:
    print("not eligible age to work")

#misc example of comparison
if 10 == '10':
    print('a')
elif "bag" > 'apple' and "bag" > "cat":
    print('b')
else:
    print('c')

#for loops
for number in range(3):
    print('attempt', number + 1, (number + 1) * '.')

print()

for number in range(1, 4):
    print('attempt', number, number * '.')

print()

for number in range(1, 10, 2):
    print('attempt', number, number * '.')

# For loop with else
attempt = False
for number in range(1, 4):
    print('attempted...' + f'{number} time')
    if attempt:
        print("Sucessful")
        break
else:
    print("Tried 3 times but couldnt able to Pass")

#Nested Loops
for x in range(3):
    for y in range(3):
        print(f"({x} , {y})")

print()
#can pass any iterable objects in for loop
for char in "Baskar":
    print(char)
print()
for list_item in [10, 20, 30, 40]:
    print(list_item)
print()
for set_item in {1, 2, 3, 4, 5}:
    print(set_item)
print()
for dict_item in {1: 10, 2: 20, 3: 30, 'D': 40}:
    print(dict_item)

#while loops
number = 15
while number > 0:
    print(number)
    number //= 2

#while loops
command = ""
print("enter quit to QUIT")
while command.lower() != 'quit':
    command = input(">>>")
    print("ECHO:", command)

#while loops - Infinite loops
command = ""
print("enter quit to QUIT")
while True:
    command = input(">>>")
    if command.lower() == 'quit':
        break
    print("ECHO:", command)


#Functions
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} .. Welcome")


def greet_return(first_name, last_name):
    return f"Hi {first_name} {last_name} .. Welcome"


print(greet("Baskar", "KS"))  #normal fun return None
greet("Sahitya", "K")  #function without return value
ret_val = greet_return("Jaasritha", "KB")  # function with return value
print(ret_val)


#keyword and default argument
def divide(number, by, add):
    return number // by + add


print(divide(10, 2, 5))
#passed value with name in function calling - keyword argument
print(divide(10, add=5, by=2))
print(divide(add=5, by=2, number=10))

print()


#default arguments (by = 1)
#value defined in function defnition is default argument
#number is "required param", by is "optional param"
#cannot define required param after optional param
def increment(number, by=1):
    return number + by


print(increment(10))
print(increment(10, 2))
print(increment(10, 4))


#X-ARGS or extended arguments
def multiply(*numbers):
    print(numbers)


multiply(10, 20, 30, 40)


def multiply(*numbers):
    print(type(numbers))
    for number in numbers:
        print(number)


multiply(10, 20, 30, 40)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(10, 20, 30))
total = multiply(10, 20, 30)
print(total)


#XX-ARGS or extended arguments for Dict
def save_user(**user):
    print(type(user))
    print(user)


def save_user(**user):
    print(type(user))
    print(user['id'])
    print(user['name'])
    print(user['age'])


save_user(id=1, name='baskar', age=22)
#save_user(1=10, 2=20, 3=30) #SyntaxError
#save_user("a" =10, "b" =20, "c" =30) #SyntaxError

#LIST CONCLUSIONS
list1 = [10, 20, 30]
print(list1)

list1 = [False, None, "Baskar", 10, 10.5, [1, 2, 3], (1, 2, 3)]
print(list1)

tuple_item = list1[len(list1) - 1]
print(tuple_item)
print(tuple_item[0])

new_list = list(('a', 'b', 'c')) * 2
print(f'doubled list : {new_list}')

empty = [0] * 10  # creat empty and initialize with default val
print(f'empty list : {empty}')

combined = empty + new_list  # can add 2 lists
print(f'added list : {combined} and length is {len(combined)}')

range_list = list(range(0, 11, 2))
print(f'range list : {range_list}')

myname_chars = list("Baskar K S")
print(f'list name chars : {myname_chars}')

# ACCESSING LIST THROUGH INDEX AND SLICE
print(myname_chars[0])  #first element
print(myname_chars[-1])  #last element
print(myname_chars[:])  #entire list
print(myname_chars[::2])
print(myname_chars[::-1])  #list in reverse

name = "Baskar"
print(name[:])

#can assign value through index
myname_chars[0] = "Bask"
print(myname_chars)
myname_chars[0] = "b"
print(myname_chars)

#0-2 replaced with 'KKK' rest 'KKK" is inserted
myname_chars[0:3] = list("KKKKKK")
print(myname_chars)

myname_chars.clear()
myname_chars = list("Baskar K S")
print(myname_chars)

#UNPACKING LIST
num_list = [888, 999]
first_num, second_num = num_list  #length both sides should match
print(first_num)
print(second_num)

#if interested only few items(first and second) in the list
first_char, second_char, *remain = myname_chars
print(first_char)
print(second_char)
print(remain)

#if interested only few items(first and last) in the list
first_char, *remain, last_char = myname_chars
print(first_char)
print(last_char)
print(remain)

#LOOPING OVER LIST
print()
print(myname_chars)

for letter in enumerate(myname_chars):
    print(type(letter), letter, letter[0], letter[1])

for index, letter in enumerate(myname_chars):
    print(f'index is {index} and character is {letter}')

# ADDING / REMOVING ELEMENTS FROM LIST
letters = list("baskar")
print(letters)
letters.append(' ')
letters.append('k')
letters.append(' ')
letters.append('s')  #add object at end
print(letters)
letters.insert(0, "name:")  # add at specific index, shifts right items
print(letters)
letters.insert(0, "full ")
print(letters)
letters.pop(0)  #remove at specific index
print(letters)
letters.append(letters.pop(0))
print(letters)
letters.pop()  # remove at end
print(letters)
letters.append("name:")
print(letters)
letters.remove("name:")  # remove based on element
print(letters)
del letters[len(letters) - 1]
print(letters)
del letters[len(letters) - 1]
print(letters)
del letters[len(letters) - 1]
print(letters)
del letters[len(letters) - 1]  #delete last element
print(letters)
letters.insert(0, "name:")
print(letters)
del letters[0]  # delete first element
print(letters)
letters.clear()  #clear the list
print(letters)

#FIND ELEMENTS IN LIST
letters = list("baskar")
print(letters)
print(letters.index('a'))  #returns index of first occurence
# print(letters.index('z')) # velue not present raise ValueError

#before getting index, check for availability
if 'k' in letters:
    print(letters.index('k'))

# SORTING LISTS
numbers = [3, 5, 2, 8, 6]
numbers.sort()  # inbuilt sort ascending
print(numbers)
numbers.sort(reverse=True)  #inbuilt sort descending
print(numbers)

#helper function, return new list. Existing list dont change
new_list = sorted(numbers)
print(new_list)
reverse_list = sorted(new_list, reverse=True)
print(f"unchanged list {new_list} and new list {reverse_list}")

#list of tuples
items = [("product1", 10), ("product2", 9), ('product3', 12)]
print(items)
items.sort()
print(f"nothing happens with inbuild sort {items}")


def get_sort_param(item):
    return item[1]  #return index1 of passed tuple item


#mention to sort based on second element of tuple item, passing key to call function
items.sort(key=get_sort_param)
print(f"sorted list based on second item of tuple {items}")

# LAMBDA FUNCTIONS
items = [('product-1', 10), ('product-2', 8), ('product-3', 15),
         ("product-4", 2), ('product-5', 14)]

items.sort(key=lambda item: item[1])
print(items)
items.sort(key=lambda item: item[1], reverse=True)
print(items)


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)

# FILTER FUNCTIONS
items = [('product-1', 10), ('product-2', 8), ('product-3', 15),
         ("product-4", 2), ('product-5', 14)]
filtered_list = []
#get and manually compare value and append to a list
for item in items:
    product, value = item
    if value >= 10:
        print(product, value)
        filtered_list.append(item)
print(filtered_list)
print(type(filtered_list[0]))

filtered_list.clear()
print(filtered_list)

print(filter(None, items))  #filter object
print(list(filter(None, items)))  # can pass function None, prints all items

#filtered using lambda functions
filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(f"Items greater than 10 => {filtered_list}")

filtered_list.clear()
filtered_list = list(filter(lambda item: item[1] <= 10, items))
print(f"Items lesser than 10 => {filtered_list}")

# MAP FUNCTION
items = [('product-1', 10), ('product-2', 8), ('product-3', 15),
         ("product-4", 2), ('product-5', 14)]
#how to get list of prices
#method-1
value_list = []
for product, value in items:
    value_list.append(value)

print(f'using method 1 : {value_list}')

value_list.clear()
print()

#method-2
for item in items:
    value_list.append(item[1])

print(f'using method 2 : {value_list}')

value_list.clear()
print()

#method-3 using map
map_obj = map(lambda item: item[1], items)
for item in map_obj:
    print(item)

print(map_obj)
value_list = list(map_obj)
#or
value_list = list(map(lambda item: item[1], items))
print(f'using method-3 using map : {value_list}')

# LIST COMPREHENSIONS
items = [('product-1', 10), ('product-2', 8), ('product-3', 15),
         ("product-4", 2), ('product-5', 14)]
# LIST COMPREHENSION
#list[expresion for item in items]
prices = [item[0] for item in items]
print(type(prices))
print(prices)
prices = [item[1] for item in items]
print(type(prices))
print(prices)
#print(list(map(lambda item: item[1], items)))

# LIST COMPREHENSION TO FILTER
filtered = [item[1] for item in items if item[1] >= 10]
print(filtered)

lists = [10,20,30,40,50,60,70,80]
comp_list = [item for item in lists if item >= 50]
print(comp_list)

# ZIP FUNCTION
list_one = [1, 2, 3, 4]
list_two = [10, 20, 30, 40]
print(zip(list_one, list_two))

print()
list_form = list(zip(list_one, list_two))
print(list_form)
print()

list_form = list(zip("ab", list_one, list_two))
print(list_form)
print()

for item in list_form:
    print(item)
print()
for val_one, val_two, val_three in list_form:
    print(val_one)
    print(val_two)
    print(val_three)
    print()

# STACKS
browsing_session = []
browsing_session.append(10)
browsing_session.append(20)
browsing_session.append(30)
browsing_session.append(40)
browsing_session.append(50)
browsing_session.append(60)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)

while len(browsing_session) > 0:
    print(f"removed element => {browsing_session.pop()}")
    if not browsing_session:
        print("stack is empty")
    else:
        print("redirect =>", browsing_session[-1])
else:
    print("Stack empty - Create new One")

# QUEUES
#FIFO => remove first element, if list is large performance degrade
from collections import deque
queue = deque([])
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)
print(queue.popleft())
print(queue)

while len(queue) > 0:
    print(f"Deque queue => {queue.popleft()}")
else:
    print("queue is empty")

# TUPLES
first = (1, 2, 3)
second = 4, 5, 6
print(type(first))
print(type(second))

fourth = 10,
print(fourth)
print(type(fourth))

point = ()
print(type(point))

#concatenate tuple
third = first + second
print(type(third))

#repeat a tuple
point = (1, 2) * 3
print(point)

#convert list to tuple
point = [10, 20, 30]
point = tuple(point)
print(type(point))
print(point)

name = "hi", "bye"
print(type(name))
print(name)

name = tuple('baskar')
print(name)
print(type(name))

#access tuple , using index and slice
point = (1, 2, 3, 4)
print(point[0])
print(point[1:3])

#unpack types, both sides quantity should be equal
x, y, z, k = point
print(x, y, z, k)

point = 10, 20, 30, 40
if 10 in point:
    print("present")

print(point[3])
# point[3] = 3 #TypeError: 'tuple' object does not support item assignment

if not point:
    print("check")

# ARRAYS
from array import array
numbers = array('i', [1, 2, 3])
print(type(numbers))
print(numbers)
#add items
numbers.append(4)
numbers.insert(0, 10)
print(numbers)
numbers.insert(8, 100)  # invalid index passed, still value added at end
print(numbers)
#remove elements
print(numbers.pop())
print(numbers.pop(1))  #pop at index 1
print(numbers)
# pass element not index to remove, invalid value is ValueError
print(numbers.remove(10))
print(numbers)

#access items
print(numbers[1])  # can access using index

# SET
# no duplicates, insertion order not preserved
numbers = [1, 2, 3, 1, 22, 2, 3, 5]
print(numbers)

#defining sets
unique = set(numbers)
using_bracket = {1, 2, 6, 5, 1, 25, 6, 7}
print("seq : {} and its type is {}".format(unique, type(unique)))
print("seq : {} its type is {}".format(using_bracket, type(using_bracket)))

#accessing set
print(unique.add(25))  # add return None
print(unique)
print(unique.remove(25))  #remove return None
print(unique)
print(unique.pop())
print(unique.pop())
print(unique.pop())
print(unique.pop())

#mathematical operations
numbers = [1, 1, 2, 3, 4]
first = set(numbers)

a, b, *c = first
print(8 * '*')
print(type(first))
print(a, b, c, type(a), type(b), type(c))
print(8 * '*')

second = {1, 6}
union = first | second  # create set about union of first and second
print(union)

intersection = first & second
print(intersection)  # create set about intersection or common elements

difference = second - first
print(difference)  #create set about uncommon difference of a - b or b - a

sym_diff = first ^ second
print(sym_diff)  # create set of symmetric difference a ^ b = a-b + b-a

# DICTIONARY
# create dictionary
#1. empty parenthesis
point = {}
print(type(point))  # not "set" its dictionary
#2. put key value pairs in parenthesis
point = {'x': 10, 'y': 20}
print(point)
print(point['x'])
#3. call dict function
point = dict(a=111, b=222)
print(point)
# print(point[a]) #NameError: name 'a' is not defined
print(point['a'])

check = {"baskar": 101, "jashi": 102}
# check = dict("baskar":101, "jashi":102) #SyntaxError: invalid syntax
# check = dict(1=10, 2=20) #SyntaxError: keyword can't be an expression
print(check["baskar"])
print(check)

#access
check["baskar"] = 1
print(check)

#add new key
check["geetha"] = 103
print(check)
print(check.keys(), type(check.keys()))

#read with invalid key using index gives error
#print(check['babu']) #KeyError: 'babu'

#first way to get value
#check key before access
if 'babu' in check:
    print(check['babu'])

if 'geetha' in check:
    print(check['geetha'])

# second way to get value with invalid key using get()
print(check.get('babu'))  # if key not present it returns None
print(check.get('babu', 0))  # if key not present return 0

#delete an item
print(check)
del check['baskar']
print(check)

#loop over dictionaries
print()
for key in check:
    print(key)  #prints only keys
print()

for item in check.items():
    print(item)  #prints keyand value in Tuple form

for key, value in check.items():  #items() return tuple of key-value pair
    print("key : {} and value : {}".format(key, value))

# DICTIONARY COMPREHENSIONS
values = []
for x in range(5):
    values.append(x)
print(values)
values = [x * x for x in values]
print(values)
values = [x * x for x in range(5)]
print(values)
values = [x * 2 for x in range(5)]
print(values)
print(type(values))

values = {x * 2 for x in range(5)}  #set
print(values)
print(type(values))

#style 1
values = {x: x * x for x in range(5)}
print(values)
print(type(values))

#style 2
values = {}
for x in range(5):
    values[x] = x * x
print(values)
print(type(values))

# TUPLE COMPREHENSIONS or GENERATORS
values = (x * x for x in range(5))
print(values)
for each in values:
    print(each)


from sys import getsizeof
values = [item * item for item in range(1000)]
print(getsizeof(values))  #4516
print(len(values))  #1000
values = (item * item for item in range(1000))
print(getsizeof(values))  #64
# cant use len() on generators
print(len(values))  #TypeError: object of type 'generator'

# UNPACKING OPERATOR
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(*numbers)

values = list(range(10))
print(values)
#unpacking operator can be applied on iterable objects

values = [*range(5), *"Baskar"]
print(values)
print(*values)

first = [1, 2, 3]
second = [4, 5]
values = [*first, 'a', *second, *"check"]
print(values)

#unpack dictionaries
first = {'x': 1}
second = {'x': 10, 'a': 10, 'b': 20}
combined = {**first, **second, 'z': 999}
print(combined)

from pprint import pprint
sentence = "this is a common interview question"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
print()
pprint(char_freq, width=1)
print()
pprint(sorted(char_freq.items()))
print()
pprint(sorted(char_freq.items(), key=lambda tup_item: tup_item[1]))
print()
pprint(
    sorted(char_freq.items(), key=lambda tup_item: tup_item[1], reverse=True))
char_freq = sorted(
    char_freq.items(), key=lambda tup_item: tup_item[1], reverse=True)
print()
print(char_freq[0])

# Exceptions
from pprint import pprint
try:
    age = int(input("Enter Age : "))
    print("print only if valid value entered")
except ValueError as ex:
    pprint("Invalid value Entered, Enter value between 1-110", width=1)
    print(ex)
    print(type(ex))
else:
    pprint("Executed only if no exception was thrown", width=1)
print("execution continued")

#Handling different exceptions
try:
    age = int(input("Enter Age : "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError) as ex:
    print("exception type {} and value : {}".format(type(ex), ex))
    print("Enter valid age between 1-110")
else:
    print("will be printed if no exception occurs")
print("Exceution continues ....")

# Handling different exceptions using finally
try:
    age = int(input("Enter Age : "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError) as ex:
    print("exception type {} and value : {}".format(type(ex), ex))
    print("Enter valid age between 1-110")
else:
    print("will be printed if no exception occurs")
finally:
    print("Cleaning all resources")
print("Exceution continues ....")

# Handling different exceptions using with block
try:
    with open("app.py") as file:
        print(file)
        print(type(file))
        print("File opened for read and closed prop")
    age = int(input("Enter Age : "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError) as ex:
    print("exception type {} and value : {}".format(type(ex), ex))
    print("Enter valid age between 1-110")
else:
    print("will be printed if no exception occurs")
print("Exceution continues ....")

# Handling different exceptions using with block multi resources
try:
    with open("app.py") as file1, open("misceleny.py", "w") as file2:
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