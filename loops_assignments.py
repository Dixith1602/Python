#Question 1: Write an if statement to check if a number is positive.

n = int(input("Enter the number: "))

if n >= 0:
    print(f"the {n} is positive")
else:
    print(f"the {n} is Negative")

#Question 2: Write an if statement to print "Even" if a number is divisible by 2.

n = int(input("Enter the number: "))

if n % 2 ==0:
    print(f"The {n} is Even")
else:
    print(f"The {n} is odd")

#Question 3: Write an if statement to check if a string is empty.

a = "Jai"

if a == "" or a == " ":
    print("The string is empty")
else:
    print("The string is not empty")

# Question 4: Use if to check if a given year is a leap year.

year = int(input("Enter the year: "))

if year % 4 == 0:
    print("The entered year is leap year")
else:
    print("The entered year is not a leap year")

# Question 5: Write an if to check if a number is greater than 100.

number = int(input("Enter the number: "))

if number > 100:
    print("The number is greater than 100")
else: 
    print("The number is not greater than 100

#Question 6: Use if to check if a character is a vowel.

word = input("Enter the charecter: ")

if word.lower() in "aeiou":
    print("The word is vowel")
else: 
    print("The word is not a vowel")

#Question 7: Write an if statement to print "Teenager" if age is between 13 and 19.

age = int(input("Enter the age: "))

if age >= 13 and age <= 19:
    print("The student is teenager")
else:
    print("The student is not a teenager")

#Question 8: Use if to check if a list has more than 5 elements.

a = [12, 21, 23, 19, 90, 67]

if len(a) >= 5:
    print("The list have min of 5 elements")
else:
    print("It has not more than 5 elements")
