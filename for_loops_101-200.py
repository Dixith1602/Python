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

#Question 151: Copy list using for loop.

list_a = [1, 2, 3, 4, 5, 6]
empty_list = []

for i in list_a:
    empty_list.append(i)

print(empty_list)

#Question 153: Print all keys of dictionary.

dct = {"name": "Dikshu", "Age": "29", "City": "Davanagere"}

for key in dct:
    print(key)

#Question 154: Print all values of dictionary.

dct = {"name": "Dikshu", "Age": "29", "City": "Davanagere"}

for value in dct.values():
    print(value)

# Question 155: Print all key–value pairs.

dct = {"name": "Dikshu", "Age": "29", "City": "Davanagere"}

for key, value in dct.items():
    print(f"{key}:{value}")

#Question 156: Count frequency of each character in string.

name = input("Enter the name: ")
freq = {}

for i in name:
    freq[i] = freq.get(i, 0) +1

print(freq)

#Question 157: Count frequency of each element in list.

list1 = [1, 2, 3, 3, 2, 4, 4, 1, 5]
freq = {}

for i in list1:
    freq[i] = freq.get(i, 0) + 1

print(freq)

#Question 158: Loop through set and print elements.

set1 = {1, 2, 3, 4, 5, 6, 7, 3, 45, 2, 3}

for i in set1:
    print(i)

#Question 159: Loop through tuple and print.

tuplee = (1, 2, 3, 4, 4, 5, 5, 6, 6)

for i in tuplee:
    print(i)

#Question 160: Print Fibonacci numbers up to 50.

fibonacci = [0, 1]

for i in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)

#Question 161: Print numbers divisible by 3 up to 100.
num3 = []
for i in range(1, 101):
    if i%3==0:
        num3.append(i)
print(num3)

#Question 162: Print numbers divisible by 7 up to 100.
num7 = []
for i in range(1, 101):
    if i%7==0:
        num7.append(i)
print(num7)

#Question 163: Print prime numbers from 1–50.

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end = ' ')

#Question 164: Print composite numbers 1–50.

for num in range(4, 51):
    for i in range(2, int(num ** 0.5) +1):
        if num%i == 0:
            print(num, end = ' ')
            break

#Question 167: Print numbers divisible by both 2 and 5.

for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end = ' ')

#Question 168: Print numbers divisible by either 2 or 5.

for i in range(1, 101):
    if i % 2 == 0 or i % 5 == 0:
        print(i, end = ' ')

#Question 169: Print numbers not divisible by 2 or 3.

for i in range(1, 101):
    if i % 2 != 0 or i % 3 != 0:
        print(i, end = ' ')

#Question 173: Print square pattern with stars.

n = 5

for i in range(1, n+1):
    for j in range(n+1):
        print("*", end = " ")
    print()

#Question 179: Print multiplication tables 1 to 10.

for num in range(1, 11):
    for i in range(1, 11):
        product=num*i
        print(f"{num}*{i}={product}")
    print("*"*50)

#Question 187: Generate list of first 10 squares.

squares = []

for i in range(1, 11):
    squares.append(i**2)
print(squares)

#Question 188: Generate list of first 10 cubes.

cubes = []

for i in range(1, 11):
    cubes.append(i**3)
print(cubes)

#Question 189: Generate list of even numbers.

even_num = []

for i in range(1, 101):
    if i%2==0:
        even_num.append(i)
print(even_num)

#Question 190: Generate list of odd numbers.

odd_num = []
for i in range(1, 101):
    if i%2!=0:
        odd_num.append(i)
print(odd_num)

#Question 191: Generate list of prime numbers.

prime_num=[]
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(num)

#Question 194: Reverse list using for.

tuplee = [1, 2, 3, 4, 4, 5, 5, 6, 6]
new_list = []

for i in reversed(tuplee):
    new_list.append(i)

print(new_list)

#Question 196: Print characters from ASCII 65–90.

for i in range(65, 91):
    print(chr(i), end = ' ')

#Question 197: Print characters from ASCII 97–122.

for i in range(97, 123):
    print(chr(i), end=' ')

#Question 198: Loop over range(5) and print numbers.

for i in range(5):
    print(i)

#Question 199: Loop over range(2, 20, 2).

for i in range(2, 20, 2):
    print(i)

#Question 200: Loop backwards using range(10, 0, -1).

for i in range(10, 0, -1):
    print(i)
