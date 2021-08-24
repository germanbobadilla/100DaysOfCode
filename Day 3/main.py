# Exercise 1 - The number you're thinking will be 10.
print("Think of a number from 0 to 100.")
a = float(input("Write the number and hit ENTER.  "))
b = float(input("Your friend gives you the same. Write it.  "))
c = float(input("I give you 20. Write it.  "))
d = float(input("Divide the the sum of the first two numbers by 2.  "))
e = float(input("Remove what your friend gave you.  "))
thinking = lambda a, b, c, e: (a + b + c) / 2 - e
print((a + b + c) / 2 - e)

# Exercise 2 - Find the modulo

number = int(input("Type the number here. "))
if number % 2 == 0:
    print("It's even.")
else:
    print("It's odd!")


# Exercise 3 - Nested

height = int(input("What is your height?  "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?  "))
    if age >= 18:
        print("You must pay $12 dollars.")
    else:
        print("Sorry. You must be 18 to ride the rollercoaster.")
else:
    print("Sorry. You can't ride the rollecoaster.")

# Exercise 4 - BMI 2.0

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
result = round(weight / height ** 2)
total = int(result)
print(f"Your BMI is: {total}")
if total >= 35:
    print("You are clinically obese.")
elif total >= 30:
    print("You are obese.")
elif total >= 25:
    print("You are overweight.")
elif total >= 18.5:
    print("You have a normal weight.")
else:
    print("You are underweight.")
    
# Exercise 5 - Leap year
year = int(input("Enter year. "))
int_year = int(year)
if int_year % 4 == 0:    
    if int_year % 100 == 0:        
        if int_year % 400 == 0:
            print(f"{int_year} is a leap year.")
        else:
            print(f"{int_year} is not a leap year.")
    else:
        print(f"{int_year} is a leap year.")
else:
    print(f"{int_year} is not a leap year.")