#Question 201: Print numbers from 1 to 10 using while.

a = 1

while a<= 10:
    print(a, end=' ')
    a+=1

#Question 202: Print numbers 10–1.

a = 10

while a>=1:
    print(a, end = ' ')
    a-=1

#Question 203: Print first 10 even numbers.

a = 0
count = 0

while count < 10:
    a+=2
    print(a, end=' ')
    count +=1

#Question 204: Print first 10 odd numbers.

a = 1
count = 0

while count < 10:
    print(a, end=' ')
    count+=1
    a+=2

#Question 205: Print sum of numbers 1–100.

a = 1
sum = 0
while a <= 100:
    sum+=a
    a+=1
print(sum)

#Question 206: Print factorial of 5 using while.

a = 1
product = 1
while a <=5:
    product*=a
    a+=1
print(product)

#Question 207: Reverse a number using while.

num = 12345
rev = 0

while num > 0:
    digit=num%10
    rev = rev * 10 + digit
    num //= 10
print(rev)

#Question 208: Sum of digits of a number using while.

num = 12345
digit_sum = 0

while num>0:
    digit = num%10
    digit_sum += digit
    num //= 10

print(digit_sum)

#Question 209: Count digits of a number using while.

num = 123456
count_digit = 0

while num > 0:
    digit = num % 10
    count_digit += 1
    num //= 10

print(count_digit)

#Question 210: Print Fibonacci series up to 50.

a = 0
b = 1

while a <= 50:
    print(a, end=' ')
    a, b = b, a+b
    
#Question 211: Print multiplication table of 8.

num = 8
a = 1

while a <=10:
    product = num*a
    print(f"{num} x {a} = {product}")
    a+=1

#Question 212: Print prime numbers up to 50.

b = 2

while b <=50:
    is_prime = True
    divisor = 2

    while divisor * divisor <= b:
        if b % divisor == 0:
            is_prime = False
            break
        divisor +=1

    if is_prime:
        print(b, end = ' ')
    b+=1

#Question 213: Print composite numbers up to 50.

a = 4

while a <= 50:
    is_prime = True
    divisor = 2

    while divisor * divisor <= a:
        if a%divisor==0:
            is_prime = False
            break
        divisor +=1
    if is_prime == False:
        print(a, end=" ")
    a+=1

#Question 214: Print numbers divisible by 7.

number = 1

while number <= 100:
    if number % 7 == 0:
        print(number, end=' ')
    number+=1

#Question 215: Print numbers not divisible by 7.

num = 1

while num <= 50:
    if num % 7 != 0:
        print(num, end=' ')
    num+=1

#Question 216: Print squares up to 100.

num = 1

while num <=100:
    sqrt_num = num**2
    print(sqrt_num, end=" ")
    num+=1

#Question 217: Print cubes up to 100.

num = 1

while num <=100:
    cube = num ** 3
    print(cube, end=" ")
    num+=1

#Question 218: Print numbers ending with digit 3.

num = 1

while num <= 100:
    if num % 10 == 3:
        print(num, end=" ")
    num+=1

#Question 219: Print numbers starting with digit 2.

num = 1

while num <= 100:
    if len(str(num)) ==2 :
        print(num, end=' ')
    num+=1

#Question 220: Print palindrome numbers between 1–200.

num = 1

while num <= 100:
    str_num = str(num)
    if str_num[0] == str_num[-1]:
        print(str_num)
    num +=1


