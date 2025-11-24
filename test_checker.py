from checker import check_strength

password = input("Enter password: ")
status, score = check_strength(password)
print(f"Strength: {status}, Score: {score}")