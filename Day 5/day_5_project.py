# Print the highest score
scores = [78, 65, 89, 86, 55, 91, 64, 89]
max_value = 0
for score in scores:
  if score > max_value:
    max_value = score

print(f"The highest score is {max_value}")

# Sume the range of number divisible by 2
result = 0
for n in range(2, 101, 2):
  print(n)
  result += n
print(result)

# Fizzbuzz
for n in range(1, 100):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")  
  else:
    print(n)

# Password generator
import random

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

print("Welcome to the PyPassword Generator!")
all = []
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


password_list = []
for char in range(1, nr_letters + 1):  
  password_list.append(random.choice(lower))
for char in range(1, nr_numbers + 1):  
  password_list.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):  
  password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ''
for char in password_list:
  password += char
print(f"Your password is: {password}")