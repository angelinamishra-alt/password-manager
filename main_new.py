from generator import generate_password
from checker import check_strength
import pyperclip

def show_menu():
    print("\n====================")
    print("  PASSWORD MANAGER  ")
    print("====================")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

print("Welcome to the Password Manager 😊")

while True:
    show_menu()
    choice = input("Enter option (1-3): ")

    if choice == "1":
        length = input("Enter password length: ")
        
        # convert safely to number
        if length.isdigit():
            pw = generate_password(int(length))
            print("\n👉 Generated Password:", pw)

            pyperclip.copy(pw)
            print("(copied to clipboard)")
        else:
            print("Please enter a number (example: 12).")

    elif choice == "2":
        pw = input("Enter a password to check: ")
        label, score = check_strength(pw)
        print("\nStrength:", label)
        print("Score:", score)

    elif choice == "3":
        print("\nThank you 💛 Goodbye!")
        break

    else:
        print("Invalid option. Try again (1, 2, or 3).")