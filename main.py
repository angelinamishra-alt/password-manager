# main.py
# This file is the main program of the Password Manager

from generator import generate_password      # for generating new passwords
from checker import check_strength           # for checking strength
from storage import add_password , load_data  # for saving and viewing passwords


def show_menu():
    print("\n=======================")
    print("     PASSWORD MENU     ")
    print("=======================")
    print("1. Generate a Password")
    print("2. Check Password Strength")
    print("3. Save a Password")
    print("4. View Saved Passwords")
    print("5. Exit")
    print("=======================")


# Program loop (runs again and again)
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # Option 1: Generate password
    if choice == "1":
        length = int(input("Enter password length: "))
        new_pw = generate_password(length)
        print("Your generated password is:", new_pw)

    # Option 2: Check strength
    elif choice == "2":
        pw = input("Enter a password to check: ")
        strength, score = check_strength(pw)
        print("Strength:", strength, "| Score:", score)

    # Option 3: Save password to storage.json
    elif choice == "3":
        service = input("Enter service name (example: Gmail): ")
        username = input("Enter username/email: ")
        pw = input("Enter password: ")

        # Basic validation
        if service == "" or pw == "":
            print("Service and Password cannot be empty.")
        else:
            add_password(service, username, pw)
            print("Password saved successfully!")

    # Option 4: View saved passwords
    elif choice == "4":
        data = load_data()
        print("\n----- Saved Passwords -----")
        for item in data["credentials"]:
            print("Service:", item["service"])
            print("Username:", item["username"])
            print("Password:", item["password"])
            print("---------------------------")

    # Option 5: Exit the program
    elif choice == "5":
        print("Thank you for using Password Manager 😊")
        break

    # If user enters anything else
    else:
        print("Invalid choice. Please try again.")
        