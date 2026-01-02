#Question 101: Use a for loop to print numbers 1 to 10.

for i in range(1,11):
    print(i)

#Question 102: Loop through a list of fruits and print each.

fruits = ['apple', 'banana', 'cherry', 'mango']

for fruit in fruits:
    print(fruit)

#Question 103: Use for to calculate sum of first 100 numbers.

sum = 0
for i in range(1,101):
    sum += i

print(sum)

#Question 104: Iterate through characters in a string.

text = input("Enter the word: ")

for i in text:
    print(i)

#Question 105: Print multiplication table of 7 using for.

num = int(input("Enter the multiplication number: "))

for i in range(1,11):
    product = num * i
    print(f"{num} X {i} = {product}")
    i +=1

#Question 106: Find factorial of a number using for.

num = int(input("enter the number: "))
factorial = 1

for i in range (1, num+1):
    factorial *= i
print(factorial)

#Question 107: Use for to count vowels in a string.

text = input("Enter the text: ")
vowel_count = 0
vowels = 'aeiouAEIOU'

for char in text:
    if char in vowels:
        vowel_count += 1

print(vowel_count)

#Question 108: Loop through dictionary keys and print.

my_dict = {"name": "Alice", "age": 30, "city": "Bangalore"}

for keys in my_dict:
    print(keys)

#Question 109: Loop through dictionary values and print.

my_dict = {"name": "Alice", "age": 30, "city": "Bangalore"}

for values in my_dict.values():
    print(values)

#Question 110: Nested for loop to print a 3x3 matrix.

for i in range(3):
    for j in range(3):
        print(i, end=" ")
    print()

#Question 111: Use for with range(10, 0, -1) to count down.

for i in range(10,0,-1):
    print(i)

#Question 112: Use for to reverse a string.

text = input("enter the text: ")
reversed_text = ''

for i in reversed(text):
    reversed_text += i

print(reversed_text)

#Question 113: Find maximum element in a list using for.

list_a = [1, 2, 3, 4, 5, 6, 66, 55, 37, 35, 76, 48]
max_value = list_a[0]

for num in list_a:
    if num > max_value:
        max_value = num
print(max_value)


