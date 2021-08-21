# What I learned this day.

## So let's work with data types

### Strings

So strings are created with double quotes. I remember that. We can pinpoint the location of a particular character by printing the string and adding square brakets, like this.

```py
    print("German Bobadilla"[5])
```

That's going to give me the letter "a".

### Integers
- Numbers inside strings can't be added. They are concatenated.

### Float
- We use floats when we want to have decimals.

### Boolean
- Easy, we have true or false.

1. We can change one data type with another.
2. To know the data typed by the user, we use the ```type``` function.
3. We can convert an int into a string by using the ```str()``` function.

### Random numbers

1. We get a random number by importing the random library.
2. To have integers in our random number and not float, use ```random.randint```.

### Mathematical operators

1. 3 + 5
2. 7 - 4
3. 3 * 2
4. Divisions results in a type float
5. PEMDAS
6. Round numbers
7. 4 // 2
8. += /= *=

### Conversion and format

1. f-String to avoid converting data types in strings.
```py
print(f"Your score is {score + 1})
```
2. Adding commas to numbers, such as: 1,924 with ```"{:,}".format()```