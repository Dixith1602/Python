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

#Question 9: Write an if statement to check if a file name ends with .txt.

words = "Please.txt"

if words.endswith(".txt"):
    print("It is")
else:
    print("No it is not")

#Question 10: Use if to check if two numbers are equal.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if a == b:
    print("Both are same")
else:
    print("No they aren't")

#Question 11: Check if a dictionary contains a key "name".

my_dict = {"name": "Alice", "age": 25}

if "name" in my_dict:
    print("Key 'name' exists.")
else:
    print("Key 'name' does not exist.")

#Question 12: Check if the sum of two numbers is greater than 50.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

c = a + b

if c > 50:
    print("The sum is greater than 50")
else:
    print("Not greater than 50")

#Question 13: Check if the first character of a string is uppercase.

word = str(input("Enter the word: "))

first_Letter = word[0]

if first_Letter.isupper():
    print("Yea the first letter is upper")
else:
    print("No, the first letter is not upper")

#Question 14: Check if temperature is below freezing (0°C).

temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("The temperature is below freezing point")
else:
    print("No it is not below freezing point")

#Question 15: Use if to check if a number is prime.

number = int(input("Enter the number: "))

if number > 1:
    for i in range(2,number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("It is not a prime number")

#Question 16: Use if to check if marks are >= 90 and print "Grade A".

marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Grade A")

#Question 17: Use if to check if password length is less than 8.

password = input("Enter the password: ")

if len(password) > 8:
    print("Password length is greater than 8")
else:
    print("Password length is not greater than 8")

#Question 18: Check if a tuple is empty.

tupel = ()

if tupel == ():
    print("Tuple is empty")
else:
    print("The tuple is not empty")

#Question 19: Check if a list contains duplicates.

list_a = [1, 2 ,3 , 4, 5]

if len(list_a) != len(set(list_a)):
    print("The list has duplicate values")
else:
    print("The list doesnt have duplicates")

#Question 20: Use if to check if string contains substring "Python".

text = "I love Python programming"

if "Python" in text:
    print("Substring found")
else:
    print("Substring not found")

#Question 21: Check if user input is numeric.

text = input("enter something: ")

if text.isnumeric():
    print("True")
else:
    print("Not number")

#Question 22: Write if to check if number is multiple of both 3 and 5.

number = int(input("Enter the number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible be 3 and 5")
else:
    print("The number is not divisible by 3 and 5")

#Question 23: Check if two strings are anagrams.

a = str(input("Enter the word: "))
b = str(input("Enter the word: "))

if sorted(a.lower()) == sorted(b.lower()):
    print("It is anagram")
else:
    print("Not anagrams")

