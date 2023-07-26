from art import calc_logo
print("Welcome to the Calculator Program")
print(calc_logo)


def add_two(a, b):
    return a + b


def add_three(a, b, c):
    return a + b + c


def add_four(a, b, c, d):
    return a + b + c + d


def subtract_two(a, b):
    return a - b


def subtract_three(a, b, c):
    return a - b - c


def subtract_four(a, b, c, d):
    return a - b - c - d

def multiply_two(a, b):
    return a * b

def multiply_three(a, b, c):
    return a * b * c

def multiply_four(a, b, c, d):
    return a * b * c * d

def div_two(a, b):
    return a / b

def div_three(a, b, c):
    return (a / b) / c

def div_four(a, b, c, d):
    return ((a / b) / c)  / d


is_on = True

while is_on:
    operation_choices = ['add', 'subtract', 'multiply', 'divide']
    entry_choices = [2, 3, 4]
    operation = input("Choose the operation you would like to perform (add, subtract, multiply, divide): ")
    while operation not in operation_choices:
        print("Please choose from options in the parentheses!!")
        operation = input("Choose the operation you would like to perform (add, subtract, multiply, divide): ")
    entry_count = int(input("How many numbers will you be entering (min of 2, max of 4): "))
    while entry_count not in entry_choices:
        print("Please choose a number between 2 and 4!")
        entry_count = int(input("How many numbers will you be entering (min of 2, max of 4): "))

    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    if operation == 'add':
        if entry_count == 2:
            print(f"The sum of {number1} and {number2} is: {number1} + {number2} = {add_two(number1, number2)}")
        elif entry_count == 3:
            number3 = int(input("Enter your third number: "))
            print(f"The sum of {number1}, {number2} and {number3} is: {number1} + {number2} + {number3} = {add_three(number1, number2, number3)}")
        else:
            number3 = int(input("Enter your third number: "))
            number4 = int(input("Enter your fourth number: "))
            print(f"The sum of {number1}, {number2}, {number3} and {number4} is: {number1} + {number2} + {number3} + {number4} = {add_four(number1, number2, number3, number4)}")
    elif operation == 'subtract':
        if entry_count == 2:
            print(f"The difference of {number1} and {number2} is: {number1} - {number2} = {subtract_two(number1, number2)}")
        elif entry_count == 3:
            number3 = int(input("Enter your third number: "))
            print(f"The difference of {number1}, {number2} and {number3} is: {number1} - {number2} - {number3} = {subtract_three(number1, number2, number3)}")
        else:
            number3 = int(input("Enter your third number: "))
            number4 = int(input("Enter your fourth number: "))
            print(f"The difference of {number1}, {number2}, {number3} and {number4} is: {number1} - {number2} - {number3} - {number4} = {subtract_four(number1, number2, number3, number4)}")
    elif operation == 'multiply':
        if entry_count == 2:
            print(f"The product of {number1} and {number2} is: {number1} * {number2} = {multiply_two(number1, number2)}")
        elif entry_count == 3:
            number3 = int(input("Enter your third number: "))
            print(f"The product of {number1}, {number2} and {number3} is: {number1} * {number2} * {number3} = {multiply_three(number1, number2, number3)}")
        else:
            number3 = int(input("Enter your third number: "))
            number4 = int(input("Enter your fourth number: "))
            print(f"The product of {number1}, {number2}, {number3} and {number4} is: {number1} * {number2} * {number3} * {number4} = {multiply_four(number1, number2, number3, number4)}")
    else:
        if entry_count == 2:
            print(f"The quotient of {number1} and {number2} is: {number1} / {number2} = {div_two(number1, number2)}")
        elif entry_count == 3:
            number3 = int(input("Enter your third number: "))
            print(f"The quotient of {number1}, {number2} and {number3} is: ({number1} / {number2}) / {number3} = {div_three(number1, number2, number3)}")
        else:
            number3 = int(input("Enter your third number: "))
            number4 = int(input("Enter your fourth number: "))
            print(f"The quotient of {number1}, {number2}, {number3} and {number4} is: (({number1} / {number2}) / {number3}) / {number4} = {div_four(number1, number2, number3, number4)}")


    another = input("Would you like to make another calculation? (y or n): ").lower()
    if another == 'n':
        is_on = False







