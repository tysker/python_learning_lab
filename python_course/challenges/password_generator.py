import random

# List of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List of 10 symbols
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# List of 10 lowercase letters
letters = [chr(i) for i in range(ord("a"), ord("a") + 10)]


print("Welcome to the PyPassword Genertor!")
password_length = int(input("How many letters would you like in your Password?\n"))
symbols_length = int(input("How many symbols would you like to have?\n"))
numbers_length = int(input("How many numbers would you like?\n"))

password = ""

for pl in range(0, password_length):
    password += random.choice(letters)
    # password += letters[pl]

for sl in range(0, symbols_length):
    password += random.choice(symbols)
    # password += symbols[sl]

for nl in range(0, numbers_length):
    password += str(random.choice(numbers))
    # password += str(numbers[nl])
    # password.append((numbers[nl]))

print(password)
