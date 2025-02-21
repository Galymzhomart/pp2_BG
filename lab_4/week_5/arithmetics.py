def add(a, b):
    return a+b

def subtract(a, b):
    if a-b < 0:
        return (a-b)*(-1)
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a > b:
        return a//b
    return b//a

