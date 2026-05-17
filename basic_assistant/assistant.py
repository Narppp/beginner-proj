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
            num1_input = input("Enter your first number (Type 'X' to exit the program): ").replace(" ", "")

            if num1_input == "X":
                print("Exiting program...")
                break
            elif not num1_input.isdigit():
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
                    print("Restarting Program...")
                    break
            print("Please wait...")
            break    
        
    elif user_pick == "Email":
        while True:
            first_name = input("Enter your first name (Type 'X' to exit the program): ").lower().replace(" ", "")

            if first_name == "x":
                print("Exiting program...")
                break
            elif first_name.isdigit() or not first_name.isalpha():
                print("First Name should not have any numbers.")
                continue
            elif len(first_name) < 4:
                print("First Name is too short, try again.")
                continue
            else:
                while True:
                    last_name = input("Enter your last name: ").lower().replace(" ", "")

                    if last_name.isdigit() or not first_name.isalpha():
                        print("Last Name should not have any numbers.")
                        continue
                    elif len(last_name) < 4:
                        print("Last Name is too short, try again.")
                        continue
                    else:
                        while True:
                            domain_list = ["@gmail.com", "@outlook.com", "@hotmail.com"]
                            for domain in domain_list:
                                print(f"{domain:>15}")

                            pick_domain = input("Choose the domain in the list: ").lower()

                            if pick_domain in domain_list:
                                full_name = first_name[:3] + last_name[-3:] + "123"
                                full_name += pick_domain
                                print(f"Your email is: {full_name}")
                                break
                            else:
                                print("Invalid domain, try again.")
                                continue 
                    print("Restarting Program...")
                    break
            print("Please wait...")
            break

    elif user_pick == "Password":
        while True:
            pass
    else:
        print("Assistant cannot do that.")
        continue

