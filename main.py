def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a % b
    if b == 0:
        return "Cannot divide by zero"
    return a / b
    
    
while True:
    
    print("\n==== SMART CALCULATOR====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multipication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Thank you")
        break
    
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice!")
        continue
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == "1":
            print("Result:", add(a, b))
            
        if choice == "2":
            print("Result:", subtract(a, b))
            
        if choice == "3":
            print("Result:", multiply(a, b))
            
        if choice == "4":
            print("Result:", divide(a, b))
            
    except ValueError:
        print("Please enter valid numbers!")
