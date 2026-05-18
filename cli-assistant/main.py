# Main File

from components.email_generator import email_generator
from components.basic_calc import basic_calc
from components.password_create import create_pass

def main_menu():
    print("Hello, I am your assistant!")
    print("Please choose the program you'd like to use today.")

    while True:
        features = ["Email Generator", "Basic Calculator", "Password Generator"]

        for num,feature in enumerate(features, start=1):
            print(f"{num}. {feature}")
        
        pick_feature = input("What do you want to do today? (Type the number to run the program): ").lower().replace(" ", "")
        
        if pick_feature == "1":
            print("Running Email Generator...")
            email_generator()
        elif pick_feature == "2":
            print("Running Calculator...")
            basic_calc()
        elif pick_feature == "3":
            print("Running Password Generator...")
            create_pass()
        else:
            print("Invalid option, try again.")
            continue
            
main_menu()


