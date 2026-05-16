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
    elif user_pick == "Email":
        while True:
            pass
    elif user_pick == "Password":
        while True:
            pass
    else:
        print("Assistant cannot do that.")
        continue

