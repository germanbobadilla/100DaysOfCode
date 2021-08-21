import random

# # Exercise 1 - Working with floats

a = float(50)
soup = float(input("How much is the soup? "))
total = a + soup
new_total = str(total)
print("The total is: " + new_total + " dollars." )

# # Exercise 2 - Random number

random_number = random.randint(0,11)
print(random_number)

# # Exercise 3 - Input 2-digit number and add them.

two_digit = input("Give me the two digits. ")
first_digit = (two_digit[0])
second_digit = (two_digit[1])
total = int(first_digit) + int(second_digit)
print(total)

# # Exercise 4 - BMI calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
result = int(weight) / float(height) ** 2
total = int(result)
print(f"Your BMI is: {total}")

# # Exercise 5 - Convert miles to kilometers

miles = input("Miles: ")
km = 1.609
kms = round(km, 2)
print(str(miles) + " miles" + " in kilometers is: " + str(int(miles) * kms) + " kms.")

# # Exercise 6 - Your age in weeks, days, and seconds

age = input("How old are you? ")
age_int = int(age)
weeks = age_int * 52
weeks_formatted = "{:,}".format(weeks)
days = age_int * 365
days_formatted = "{:,}".format(days)
seconds = days * 86400
secs_formatted = "{:,}".format(seconds)
print(f"You are {weeks_formatted} weeks, {format(days_formatted)} days and {secs_formatted} seconds old.")

# Exercise 7 - Tip calculator

total = float(input("What was the total bill?  "))
tip = int(input("What percentage tip would you like to give: 10, 12, or 15?  "))
people = int(input("How many people to split the bill into?  "))
tip = tip / 100 * total
final_total = total + tip
split = round(final_total / people, 2)
print(f"Each person should pay: ${split}")