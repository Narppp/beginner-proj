# Basic Calculator

def basic_calc():
    print("Welcome to the Calculator!")
    
    while True:
        num1 = input("Enter your first number (or type 'X' to exit the program): ").replace(" ", "")
        
        if num1 == "X":
            print("Exiting program...")
            return
        elif not num1.isdigit():
            print("Invalid number, try again.")
            continue
        else:
            break
        
    while True:
        num2 = input("Enter your second number: ").replace(" ", "")
        
        if not num2.isdigit():
            print("Invalid number, try again.")
            continue
        else:
            break
            
    while True:
        operators = ["+", "-", "*", "/"]
        user_operator = input("Choose your operator ('+', '-', '*', '/'): ").replace(" ", "")
         
        if user_operator == operators[0]:
            result = int(num1) + int(num2)
            print(f"Result: {result}")
            return result
        elif user_operator == operators[1]:
            result = int(num1) - int(num2)
            print(f"Result: {result}")
            return result
        elif user_operator == operators[2]:
            result = int(num1) * int(num2)
            print(f"Result: {result}")
            return result
        elif user_operator == operators[3]:
            result = int(num1) / int(num2)
            print(f"Result: {round(result, 2)}")
            return result
        else:
            print("Invalid operator, try again.")
            continue
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            