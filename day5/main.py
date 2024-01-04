#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_letters = []
password_symbols = []
password_numbers = []

# Generates random letters, symbols and lettters
for _ in range (nr_letters):
  password_letters.append(random.choice(letters))

for _ in range (nr_symbols):
  password_symbols.append(symbols[random.randint(0,len(symbols)-1)])

for _ in range (nr_numbers):
  password_numbers.append(numbers[random.randint(0,len(numbers)-1)])

# Combines list to create a master password list
password_master = password_letters + password_symbols + password_numbers
print(''.join(password_master))

# Randomise order of password
random.shuffle(password_master)
print(''.join(password_master))
