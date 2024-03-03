#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_list = []
for letter in range(1, nr_letters + 1):
  selected_letters = random.choice(letters)
  password_list.append(selected_letters)
  
for symbol in range(1, nr_symbols + 1):
  selected_symbol = random.choice(symbols)
  password_list.append(selected_symbol)
  
for num in range(1, nr_numbers + 1):
  selected_number = random.choice(numbers)
  password_list.append(selected_number)

for password in password_list:
  password_string = ''.join(password_list)

# Convert the list into a single string
print(f"Your password is : {password_string}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password_list)
#randomized_string = ''.join(password_list)

password = ""
for char in password_list:
  password += char
print(f"Your randomized password is : {password}")
