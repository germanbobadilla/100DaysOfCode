# A quiz to help you decide your undergraduate studies.

cs_score = 0
es_score = 0

def start():
    print("You got equal points in Earth Science and Computer Science.\n"
          + "Let's see how you do in this quiz.\n"
          + "The most points you get in one, that's what you should study. ")
    quiz()
def quiz():
    ## First Questions
    print("Question 1")
    print("Who was the second CEO of Apple Computers?")
    print("Write the letter to make a choice.")
    print("a) Mike Markulla")
    print("b) Steve Wozniak")
    print("c) Nolan Bushnell")
    q1 = input()
    if q1 == "a":
        cs_score =+ 50
    elif q1 == "b":
        cs_score =- 15
    elif q1 == "c":
        cs_score =- 15
    else:
        print("That's not a letter. Let's begin. \n \n \n \n")
        quiz()
    ## Second questions
    print("Question 2.")
    print("_____ refers to the expiration of water through the minute pores or stomata of trees.")
    print("Write the letter to make a choice.")
    print("a) Consumation")
    print("b) Transpiration")
    print("c) Evaporation")
    q2 = input()
    if q2 == "b":
        es_score =+ 50
    elif q2 == "a":
        es_score =- 15
    elif q2 == "c":
        es_score =- 15
    else:
        print("That's not a letter. Let's begin.")
        quiz()
    ## Third questions
    print("Question 3.")
    print("The _____ refers to the transfer of water from one state or reservoir to another.")
    print("Write the letter to make a choice.")
    print("a) Rock Cycle")
    print("b) Biogeochemical Cycle")
    print("c) Water Cycle")
    q3 = input()
    if q3 == "c":
        es_score =+ 50
    elif q3 == "a":
        es_score =- 15
    elif q3 == "b":
        es_score =- 15
    else:
        print("That's not a letter. Let's begin.")
        quiz()
    ## Fourth questions
    print("Question 4.")
    print("What was the search engine Google initially written in?")
    print("Write the letter to make a choice.")
    print("a) Java")
    print("b) Python")
    print("c) C++")
    q4 = input()
    if q4 == "b":
        cs_score =+ 50
    elif q4 == "a":
        cs_score =- 15
    elif q4 == "c":
        cs_score =- 15
    else:
        print("That's not a letter. Let's begin.")
        quiz()
    print(f"You got: {cs_score} in Computer Science, and {es_score} in Earth Science.")
    if cs_score > es_score:
        print("You should study Computer Science.")
    elif es_score > cs_score:
        print("You should study Earth Science.")
    elif es_score == cs_score:
        print("You got equal points. You can study whatever you want.")
start()