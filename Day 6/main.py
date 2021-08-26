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
