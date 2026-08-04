import random
import string

print("====================================")
print("    RANDOM PASSWORD GENERATOR")
print("====================================")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nSelect character types to include:")
        upper = input("Include Uppercase letters? (y/n): ").lower()
        lower = input("Include Lowercase letters? (y/n): ").lower()
        numbers = input("Include Numbers? (y/n): ").lower()
        symbols = input("Include Symbols? (y/n): ").lower()

        characters = ""
        selected = 0

        if upper == "y":
            characters += string.ascii_uppercase
            selected += 1

        if lower == "y":
            characters += string.ascii_lowercase
            selected += 1

        if numbers == "y":
            characters += string.digits
            selected += 1

        if symbols == "y":
            characters += string.punctuation
            selected += 1

        if selected < 2:
            print("\nPlease select at least TWO character types.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using the Password Generator!")
            break

    except ValueError:
        print("\nInvalid input! Please enter a valid number.")