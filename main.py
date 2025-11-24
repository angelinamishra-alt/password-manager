from generator import generate_password
from checker import check_strength
from history import add_password , load_data

def show_menu():
    print("\n===========================")
    print("     PASSWORD MANAGER      ")
    print("===========================")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Save Password")
    print("4. View Saved Passwords")
    print("5. Exit")
    print("===========================\n")


while True:
    show_menu()
    choice = input("Enter option (1-5): ")

    # Option 1 — Generate
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            pw = generate_password(length)
            print("\nGenerated Password:", pw)
        except:
            print("Please enter a valid number.")

    # Option 2 — Check strength
    elif choice == "2":
        pw = input("\nEnter password to check: ")
        label, score = check_strength(pw)
        print(f"Strength: {label} (Score: {score})")

    # Option 3 — Save password
    elif choice == "3":
        service = input("Service (example: Gmail, Instagram): ")
        username = input("Username / email: ")
        pw = input("Password: ")

        if service == "" or pw == "":
            print("Service and password cannot be empty!")
        else:
            add_password(service, username, pw)
            print("\nPassword Saved Successfully ✔")

    # Option 4 — View saved passwords
    elif choice == "4":
        data = load_data()
        print("\n--- SAVED PASSWORDS ---")
        for item in data["credentials"]:
            print(f"{item['service']} | {item['username']} | {item['password']}")
        print("------------------------")

    # Option 5 — Exit
    elif choice == "5":
        print("\nThank you for using Password Manager 💛")
        break

    else:
        print("\nInvalid option. Try again.")