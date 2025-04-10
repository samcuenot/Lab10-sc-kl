# https://github.com/samcuenot/Lab10-sc-kl.git
# Partner 1: Samantha Cuenot
# Partner 2: Kayla Le
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    return math.log(a, b)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)