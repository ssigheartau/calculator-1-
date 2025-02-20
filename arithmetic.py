"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    summation = num1 + num2 
    return summation


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    subtraction = num1 - num2
    return subtraction

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    multiplication =  num1 * num2 
    return multiplication

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    if num2 != 0:
      division = num1 / num2
      return division
    else:
      return "Error: Division by zero"

def square(num1):
    """Return the square of num1."""
    squ = num1 ** 2
    return squ

def cube(num1):
    """Return the cube of num1."""
    cub = num1 ** 3
    return cub

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    pow = num1 ** num2
    return pow

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    if num2 != 0:
      mod = num1 % num2
      return mod
    else:
      return "Error: Modulo by zero"