def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Enter choice (0/1/2/3/4): ")

    if choice == '0':
        print("Goodbye!")
        break
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
            print("Invalid number! Try again.")
            continue
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
            print("Invalid number! Try again.")
            continue

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")