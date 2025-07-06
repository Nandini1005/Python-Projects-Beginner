# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    return a / b

while True:
    print("\nChoose operation: +, -, *, / or type 'exit' to quit")
    choice = input("Enter operator: ")

    if choice == 'exit':
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Please try again.")
        continue

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")
