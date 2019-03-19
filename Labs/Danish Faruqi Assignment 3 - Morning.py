# Danish Faruqi  - Morning Class



import math
# The user must make the inputs, not the programmer.
# Make a single script file that includes example results as comments.

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Problem 1
#  Write a python program to print The Collatz Conjecture starting from the given number n.
# Handle invalid inputs. (Do NOT use while/for loops.) (40pts)

def collatz(n): #Have to be natural numbers
    print(n)
    if (n <= 0):
        return

    if n != 1:

        if n % 2 == 0:
            n = n / 2

        elif n % 2 == 1:
            n = ((3 * n) + 1)

    elif n == 1:
        return

    collatz(int(n))

# Exnamples :
# collatz(7) --> 7 22 11 34 17 52 26 13 40 20 10 5 16 8 42 1

# collatz(0) --> 0

# collatz(-5) --> -5

# collatz(6) --> 6 3 10 5 16 8 4 2 1

# User Input

w = int(input("The The Collatz Conjecture, Enter a number : "))
collatz(w)




#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# division by zero error, type error, name error?

# Problem 2
# The Python3 program below crashes in some conditions.
# Modify the program and prevent it from crashing for all of these conditions. (30pts)

print(' ')
print(' Start Division')
try:
    a = int(input("Enter a Number : "))
    b = int(input("Input a Number : "))
    print(a / b)
except ZeroDivisionError as e:
    print('Error,',  e, 'occured')
except ValueError as e:
    print('Error,', e)

# Exnamples :
#  a = '2' --> Error, invalid literal for int() with base 10: "'2'"
#  b = 3.0 --> Error, invalid literal for int() with base 10: '3.0'
#  b = 0 --> Error, division by zero occured
#  a = 10, b = 5 --> 2.0

# User Input



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Problem 3
# Write a Python program to print all prime factors of a number n. (Do not use Python lists. You may
# print duplicate factors) (15pts)

print(' ')
n = int(input("Put in a Number you want to see all the prime factors of : "))

if n%2 == 1 and n != 0:
    for counter in range(3, int(math.sqrt(n)) + 1, 2): #odd
        while n % counter == 0:
             print(int(counter))
             n = n / counter
    #even
if n%2 == 0 and n != 0:
    while n % 2 == 0:
         print(2)
         n = n / 2

if n > 2:
    print(int(n))
if n ==0:
    print(0)

#Example
# n = 0 --> 0
# n = 10 --> 2, 5

#User Input

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' ')
# Problem 4
# Write a Python function to print all prime numbers that are less than or equal to some number n. (Do
# not use Python lists) (15pts)
def list_prime(n):
    if n > 1:
        for counter in range(2,n + 1):
           if counter > 1:
               for i in range(2,counter):
                   if (counter % i) == 0:
                       break
               else:
                   print(counter)
    else:
        print(n)

# Example
# list_prime(7 --> 2 3 5 7


# User Input
list_prime(int(input('Enter number to print all prime numbers less than or equal to it : ')))