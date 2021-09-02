# A very simple password generator

import random
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
non_alpha = [',', '.', '<', '>', '?', '/', ';', ':', ']', '[',
             '{', '}', '|', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

merged_lists = lower + capital + non_alpha + numbers
password_length = int(input("How long you want your password to be?  "))
for i in range(1):    
    password_list = random.choices(merged_lists, k=password_length)

password = ''.join([str(item) for item in password_list])
print(f"This is your new password: {password}")