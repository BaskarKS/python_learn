def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return input


while True:
    number = input("Enter a Number|q to quit: ")
    if number.lower() == "q":
        break
    print(fizzbuzz(int(number)))