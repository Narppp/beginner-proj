# Basic Assistant

print("Hello, I am your assistant for today.")
print("Here's everything i can do:")
print("1. Basic Calculator")
print("2. Email Generator")
print("3. Password Generator")

while True:
    user_pick = input("Choose what you want to do (Type Calculator, Email, or Password): ").capitalize().strip()

    if user_pick == "Calculator":
        while True:
            num1_input = input("Enter your first number: ").replace(" ", "")

            if not num1_input.isdigit():
                print("Invalid number, try again.")
                continue
            else:
                num1_input = int(num1_input)
                while True:
                    num2_input = input("Enter your second number: ").replace(" ", "")

                    if not num2_input.isdigit():
                        print("Invalid number, try again.")
                        continue
                    else:
                        num2_input = int(num2_input)
                        while True:
                            pick_operation = input("Choose your operation (+, -, *, /): ")

                            if pick_operation == "+":
                                result = num1_input + num2_input
                                print(f"Result: {result}")
                                break
                            elif pick_operation == "-":
                                result = num1_input - num2_input
                                print(f"Result: {result}")
                                break
                            elif pick_operation == "*":
                                result = num1_input * num2_input
                                print(f"Result: {result}")
                                break
                            elif pick_operation == "/":
                                result = num1_input / num2_input
                                print(f"Result: {round(result, 2)}")
                                break
                            else:
                                print("Invalid operation, try again.")
                                continue
                    try_again = input("Want to try the calculator again? (Y/N): ").title().replace(" ", "")

                    if try_again == "Y":
                        break
                    elif try_again != "N":
                        print("Invalid option, exiting program...")
                        exit()
                    else:
                        print("Restarting Program...")
                        break
            print("Please wait...")
            break
                    
        
    elif user_pick == "Email":
        while True:
            pass
    elif user_pick == "Password":
        while True:
            pass
    else:
        print("Assistant cannot do that.")
        continue

