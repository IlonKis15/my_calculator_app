import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    operation = sys.argv[1]
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])

    if operation == "add":
        print(add(num1, num2))
    elif operation == "subtract":
        print(subtract(num1, num2))
    elif operation == "multiply":
        print(multiply(num1, num2))
    elif operation == "divide":
        print(divide(num1, num2))
    else:
        print("Unsupported operation")
