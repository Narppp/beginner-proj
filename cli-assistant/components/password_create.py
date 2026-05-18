# Password Creator

def create_pass():
    print("Welcome to Password Generator!")
    
    while True:
        create_pass = input("Create your password (or type 'X' to exit the program): ").replace(" ", "")
        
        if create_pass == "X":
            print("Exiting program...")
            return
        elif len(create_pass) < 7:
            print("Short password, try again.")
            continue
        elif len(create_pass) > 7 and create_pass.isalpha():
            print("Try mixing letters with numbers for a stronger password.")
            continue
        elif len(create_pass) > 7 and create_pass.isdigit():
            print("Try mixing numbers with letters for a stronger password.")
            continue
        else:
            print(f"Created Password: {create_pass}")
            return create_pass
    