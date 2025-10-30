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

history =[] 

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. History")
    print("0. Exit")

    choice = input("Enter choice (0/1/2/3/4/5): ")

    
    if choice == '0':
        print("Goodbye!")
        break

    if choice == '5':
        if history:
            print("\nHistory:")
            for record in history:
                print(record)
        else:
            print("No calculations yet.")
        break
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid number! Please enter digits only.")
        continue

    if choice == '1':
        result = add(num1, num2)
        print("Result:", add(num1, num2))
        history.append(f"{num1} + {num2}={result}")
    elif choice == '2':
        result = add(num1, num2)
        print("Result:", subtract(num1, num2))
        history.append(f"{num1} - {num2}={result}")
    elif choice == '3':
        result = add(num1, num2)
        print("Result:", multiply(num1, num2))
        history.append(f"{num1} * {num2}={result}")
    elif choice == '4':
        result = add(num1, num2)
        if num2 == 0:
            print("Cannot divide by zero.Try again")
        print("Result:", divide(num1, num2))
        history.append(f"{num1} / {num2}={result}")
    else:
        print("Invalid choice")
    