#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Jonathan Jones"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    product = 0
    if x > 0 and y > 0:
        for num in range(x):
            product = add(product, y)
        return product
    elif x < 0 and y < 0:
        for num in range(x, 0):
            product = add(product, y)
        return abs(product)
    elif x < 0 and y > 0:
        for num in range(x, 0):
            product = add(product, -y)
        return product
    elif x > 0 and y < 0:
        for num in range(y, 0):
            product = add(product, -x)
        return product


def power(x, n):
    """Raise x to power n, where n >= 0"""
    count = n
    if n > 0 and x > 0:
        result = 1
        while count:
            result = multiply(result, x)
            count = count - 1
        return result
    elif n > 0 and x < 0:
        result = 1
        while count:
            result = multiply(result, x)
            count = count - 1
        return result
    elif x == 0:
        return 0
    else:
        return 1


def factorial(x):
    """Compute factorial of x, where x > 0"""
    total = 1
    count = x
    while count:
        total = multiply(count, total)
        count = count - 1
    return total


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    num_1 = 0
    num_2 = 1
    result = 0
    if n == 1:
        return 1
    else:
        for num in range(1, n):
            result = add(num_1, num_2)
            num_1 = num_2
            num_2 = result
        return result


if __name__ == '__main__':
    # your code to call functions above
    add(2, 4)
    multiply(6, -8)
    power(2, 8)
    factorial(4)
    fibonacci(8)