import time
import pprint

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    return (a/b, a%b)

def sub(a, b):
    return a - b

num1 = 5
num2 = 7

sum = add(num1, num2)
print("Sum = ", sum)

prod = mult(num1, num2)
print("Product = ", prod)

quot, rem = div(num1, num2)
print("Quotient = ", quot, "\nRemainder = ", rem)

diff = sub(num1, num2)
print("Difference = ", diff)
