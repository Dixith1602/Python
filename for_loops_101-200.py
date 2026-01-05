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

#Question 114: Copy elements of one list to another using for.

list_a = [1, 2, 3, 4, 5, 6, 66, 55, 37, 35, 76, 48]
list_b = []

for item in list_a:
    list_b.append(item)

print(list_b)

#Question 115: Generate a list of squares using for.

list_a = [1, 2, 3, 4, 5, 6]
list_b = []

for i in list_a:
    list_b.append(i**2)

print(list_b)

#Question 116: Loop to print Fibonacci numbers up to 50.

a, b = 0, 1

for i in range (20):
    if a > 50:
        break
    print(a, end = ' ')
    a, b = b, b + a

#Question 117: Print only even numbers from 1–50 using for.

for i in range(51):
    if i % 2 == 0:
        print(i)

#Question 118: Print index and value of a list using enumerate.

list_a = [1, 2, 3, 4, 5, 6]

for index, values in enumerate(list_a):
    print(f"index {index}: {values}")

#Question 119: Iterate over two lists at once using zip.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

#Question 120: Find common elements in two lists using for.

list_a = [1, 2, 3, 4, 5, 6]
list_b = [1, 2, 3, 4, 5, 6, 66, 55, 37, 35, 76, 48]
common = []

for i in list_a:
    for j in list_b:
        if i == j:
            if i not in common:
                common.append(i)

print(common)

#Question 121: Print numbers 1–10.

for i in range (11):
    print(i)

#Question 122: Print numbers 10–1.

for i in range(10, 0, -1):
    print(i)

#Question 123: Print first 20 even numbers.

for i in range(1, 41):
    if i % 2 == 0:
        print(i)

#Question 124: Print first 20 odd numbers.

for i in range(1, 41):
    if i % 2 != 0:
        print(i)

#Question 125: Print squares of numbers 1–10.

for i in range(1, 11):
    print(i**2)

#Question 126: Print cubes of numbers 1–10.

for i in range(1, 11):
    print(i**3)

#Question 127: Print multiplication table of 5.

num = 5

for i in range(1, 11):
    product = num * i
    print(f"{num} X {i} = {product}")

#Question 128: Print multiplication table of any number.

num = int(input("Enter the multiplication number: "))

for i in range(1,11):
    product = num * i
    print(f"{num} X {i} = {product}")
    i +=1

#Question 129: Print factorial of 6 using for.

num = 6
factorial = 1

for i in range(1, num+1):
    factorial *= num
print(factorial)

#Question 130: Calculate sum of first 100 numbers.

total = 0

for i in range (1,101):
    total += i

print(total)

#Question 131: Calculate product of first 10 numbers.

product = 1

for i in range(1, 11):
    product*=i

print(product)


#Question 132: Print characters of a string one by one.

text = input("Enter the text: ")
str_text = str(text)

for i in str_text:
    print(i)

#Question 133: Reverse a string using for.

text = input("Enter the text: ")
reversed_text = ""

for i in reversed(text):
    reversed_text+=i

print(reversed_text)

#Question 134: Count vowels in a string.

text = input("Enter the text: ")
vowel_count = 0
vowels = 'aeiouAEIOU'

for char in text:
    if char in vowels:
        vowel_count += 1

print(vowel_count)

#Question 135: Count consonants in a string.


text = input("Enter the text: ")
consonants_count = 0
vowels = 'aeiouAEIOU'

for char in text:
    if char not in vowels:
        consonants_count += 1

print(consonants_count)

#Question 136: Count digits in a string.

text = input("Enter the text: ")
count_digits = 0
digits = '1234567890'

for i in text:
    if i in digits:
        count_digits+=1
print(count_digits)

#Question 137: Count spaces in a string.

text = input("Enter the text: ")
count_space = 0
space = " "

for i in text:
    if i in space:
        count_space += 1
print(count_space)

#Question 138: Print list elements one by one.

list_a = [1, 2, 3, 4, 5, 6]

for i in list_a:
    print(i)

#Question 139: Find sum of all list elements.

list_a = [1, 2, 3, 4, 5, 6]
sum = 0
for i in list_a:
    sum+=i
    
print(sum)

#Question 140: Find maximum in a list.

list_a = [1, 2, 3, 4, 5, 6]
max_value = list_a[0]

for i in list_a:
    if i > max_value:
        max_value = i
print(max_value)

#Question 141: Find minimum in a list.

list_a = [1, 2, 3, 4, 5, 6]
min_value = list_a[0]

for i in list_a:
    if i < min_value:
        min_value = i
print(min_value)

#Question 142: Print index and value of list.

list_a = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(list_a):
    print(f"index {index}: {value}")

#Question 143: Print elements at even indexes.

list_a = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(list_a):
    if index%2==0:
        print(f"index {index}: {value}")

#Question 144: Print elements at odd indexes.

list_a = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(list_a):
    if index%2!=0:
        print(f"index {index}: {value}")

#Question 145: Double every element in list.

list_a = [1, 2, 3, 4, 5, 6]

for i in list_a:
    print(i+i)

#Question 146: Square every element in list.

list_a = [1, 2, 3, 4, 5, 6]

for i in list_a:
    print(i**2)

#Question 147: Filter even numbers from list.

list_a = [1, 2, 3, 4, 5, 6]

for index, values in enumerate(list_a):
    if values % 2 == 0:
        print(f"index {index}: {values}")

#Question 148: Filter odd numbers from list.

list_a = [1, 2, 3, 4, 5, 6]

for index, values in enumerate(list_a):
    if values % 2 != 0:
        print(f"index {index}: {values}")

#Question 149: Print common elements in two lists.
list_a = [1, 2, 3, 4, 5, 6]
list_b = [1,3,5,7,9,8]
common_elements = []

for i in list_a:
    for j in list_b:
        if i == j:
            if i not in common_elements:
                common_elements.append(i)
print(common_elements) 

#Question 150: Print unique elements from list.

list_a = [1, 2, 3, 4, 5, 6]
list_b = [1,3,5,7,9,8]
non_common = []

for i in list_a:
    if i not in list_b and i not in non_common:
        non_common.append(i)
for i in list_b:
    if i not in list_a and i not in non_common:
        non_common.append(i)

print(non_common)

#Question 151: Copy list using for loop.

list_a = [1, 2, 3, 4, 5, 6]
empty_list = []

for i in list_a:
    empty_list.append(i)

print(empty_list)
