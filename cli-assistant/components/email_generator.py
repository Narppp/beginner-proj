# Basic Email Generator

def email_generator():
    print("Welcome to Email Generator!")
    while True:
        first_name = input("Enter your first name (or type 'X' to exit the program): ").lower().replace(" ", "")
        
        if first_name == "":
            print("The input should not be empty.")
            continue
        elif first_name == "x":
            print("Exiting program...")
            return
        elif not first_name.isalpha():
            print("Invalid name, try again.")
            continue
        elif len(first_name) < 2:
            print("Name too short, try again.")
            continue
        else:
            break
    
    while True:
        birth_year = input("Enter your birthyear (Ex: 2006): ")
        if not birth_year.isdigit() or len(birth_year) != 4:
            print("Invalid birth year, try again.")
            continue
        else:
            break
    
    domains = ["@gmail.com", "@outlook.com", "@hotmail.com"]
    
    for num,domain in enumerate(domains, start=1):
        print(f"{num}. {domain}")
        
    while True:
        choose_domain = input("Type the domain of your email: ")
        
        if choose_domain in domains:
            break
        else:
            print("Invalid domain, try again.")
            continue
     
    user_email = first_name[:3] + birth_year[-3:] + choose_domain
    print(f"Created Email: {user_email}")
    print("Exiting Program...")
    return user_email
    