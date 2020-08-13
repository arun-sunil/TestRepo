import time
import pprint
# Testing PR File List

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    return a/b

def sub(a, b):
    return a - b

num1 = 5
num2 = 7

sum = add(num1, num2)
time.sleep(5)
print("Sum = ", sum)

prod = mult(num1, num2)
print("Product = ", prod)

quot = div(num1, num2)
print("Quotient = ", quot)

diff = sub(num1, num2)
print("Difference = ", diff)
