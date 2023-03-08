# lab06software.py
# By: Rachel Estrada
# Course #: COP3502 - Programming Fundamentals 1
# ID#: 18254685

# Start out with the definition or encoder/decoder
def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


def decoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result


# Next is the main function followed by 3 print statements
def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")

        # Declare an input as a variable
        choice = input("Enter your choice (1 or 2 or 3): ")
        if choice == "1":
            value = input("Enter an 8-digit password: ")
            print("Encoded password is", encoder(value))
        elif choice == "2":
            value = input("Enter an already encoded 8-digit password: ")
            print("Decoded password is", decoder(value))
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()

    # End with main
    main()
