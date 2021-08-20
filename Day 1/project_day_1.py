# Project
# I created a bot that combines the name of parents
# to give it to their future offspring.

print("Bot: I can help you with your child name.") # The bot's helping out
she_or_he = input("Bot: Is it a she or a he? ").lower() # A var that holds the input
she_or_he = she_or_he.strip()

if she_or_he == "he":    # Depending on the input, if it's a boy
    print("Bot: Great! Let's find a name for your baby boy")    
    spose_name1 = input("What's your spouse name? ") # Saves the value in var
    spose_name2 = input("What's your name? ")
    first_three_char1 = spose_name1[0:3].lower() # Takes the first three letters of the name
    first_three_char2 = spose_name2[0:3].lower() # Changes it to lowercase    
    print("Wonderful! The name is " + first_three_char1.capitalize() + first_three_char2 + ".\nDo you think he'll like it?")
elif she_or_he == "she": # If it's a baby girl
    she = "she"
    print("Bot: Great! Let's find a name for your baby girl")    
    spose_name1 = input("What's your spouse name? ") # Saves the value in var
    spose_name2 = input("What's your name? ")
    first_three_char1 = spose_name1[0:3].lower() # Takes the first three letters of the name
    first_three_char2 = spose_name2[0:3].lower() # Changes it to lowercase    
    print("Wonderful! The name is " + first_three_char1.capitalize() + first_three_char2 + ".\nDo you think she'll like it?")
    # Prints the first three letters of each parent capitalized