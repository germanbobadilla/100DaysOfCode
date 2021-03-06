# Nested lists

brothers = ['German', 'El latin', 'Basilio']
older_brothers = ['Momon', 'James']

nested_list = [brothers, older_brothers]

print(nested_list[0])

# Exercise 3 - Treasure map

row1 = ['🤍', '🤍', '🤍']
row2 = ['🤍', '🤍', '🤍']
row3 = ['🤍', '🤍', '🤍']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to go to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

heart = '❤️'

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = heart


print(f"{row1}\n{row2}\n{row3}\n")

# Exercise 4

import math

def paint_calc(height,width,cover):

    num_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
    
paint_calc(13, 90, 35)

# Exercise 5 Capitalize your name

def capitalizar(x: str):    
    word = x    
    return word.capitalize()

print(capitalizar('german'))

# Exercise 6, how old(days) are you?
import datetime

def days_alive(m: int, d: int, y: int):
    now = datetime.datetime.now()    
    age = now.year - y
    days_in_years = age * 365
    days_in_months = m * 30
    total_days = days_in_years + days_in_months + d
    return total_days

daysalive = "{:,}".format(days_alive(5, 11, 1992))
print(daysalive)

