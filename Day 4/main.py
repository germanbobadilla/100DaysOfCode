# Exercise 1 - Pizza order

print("Welcome to Pizza German")
sp = 15
mp = 20
lp = 25
ppsp = 2
ppmp_and_lp = 3
ec = 1
bill = 0

size = input("What size pizza do you want? S, M, or L  ")
if size == "s":
    bill += sp
    add_pepperoni = input("Do you want pepperoni? Y or N  ")
    if add_pepperoni == "y":
        bill += ppsp
    extra_cheese = input("Do you want extra cheese? Y or N  ")
    if extra_cheese == "y":
       bill += ec
       print(f"Your total bill is {bill}.")
elif size == "m":
    bill += mp
    add_pepperoni = input("Do you want pepperoni? Y or N  ")
    if add_pepperoni == "y":
        bill += ppmp_and_lp
    extra_cheese = input("Do you want extra cheese? Y or N  ")
    if extra_cheese == "y":
       bill += ec
       print(f"Your total bill is {bill}.")
elif size == "l":
    bill += lp
    add_pepperoni = input("Do you want pepperoni? Y or N  ")
    if add_pepperoni == "y":
        bill += ppmp_and_lp
    extra_cheese = input("Do you want extra cheese? Y or N  ")
    if extra_cheese == "y":
       bill += ec
       print(f"Your total bill is {bill}.")
else:
    print(f"Your total bill is {bill}.")
    
# Exercise 2 - Rock paper scissors

import random

rock_scissors = "Wins"
scissors_paper = "Wins"
paper_rock = "Wins"

def game1():
    mylist = ["Rock", "Paper", "Scissors"]    
    player1 = random.choice(mylist)
    player2 = random.choice(mylist)
    print(f"Player 1: {player1} | Player 2: {player2}")
    if player1 == player2:        
        print(f"You've got yourselves a tie.")

    if player1 == "Rock" and player2 == "Scissors":
        print(f"Player 1, you win.")
    if player1 == "Scissors" and player2 == "Paper":
       print(f"Player 1, you win.")
    if player1 == "Paper" and player2 == "Rock":
       print(f"Player 1, you win.")        
    if player2 == "Rock" and player1 == "Scissors":
        print(f"Player 2, you win.")
    if player2 == "Scissors" and player1 == "Paper":
        print(f"Player 2, you win.")
    if player2 == "Paper" and player1 == "Rock":
        print(f"Player 2, you win.")
game1()