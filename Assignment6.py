# 1. The Calculator App
# Objective: Build a basic calculator for addition, subtraction, multiplication, and division.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter choice (1/2/3/4): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    if operation == '1':
        print(f"Result: {add(num1, num2)}")
    elif operation == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")

# 2. The Shopping List Maker
# Objective: Create a program that helps users manage a shopping list.

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(item):
    try:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    except ValueError:
        print(f"{item} is not in the list.")

def print_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def shopping_list_maker():
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            remove_item(item)
        elif choice == '3':
            print_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# To run the calculator or shopping list maker, uncomment the desired function call below.

# calculator()
# shopping_list_maker()
