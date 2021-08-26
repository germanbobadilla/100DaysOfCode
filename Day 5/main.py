# Exercise 1 - Heads or tales
import random

result = random.randint(0, 1)
if result == 0:
    print("Heads")
else:
    print("Tails")

# Exercise 2 - Appending a list

user_input = []
name = input("What's your name? ")
user_input.append(name)
age = int(input("What's your age? "))
user_input.append(age)
undergraduate = input("Are you an undergraduate student? Yes, or No ")
user_input.append(undergraduate)

print("Updated List : ", user_input)

# Exercise 3 - Who's paying for the bill.
import random
people = ["German", "El Latin", "Basilio"]
number_of_people = len(people)
random_person = random.randint(0,number_of_people -1)
payer = people[random_person]
print(f"{payer} is going to pay for the bill. Haha.")