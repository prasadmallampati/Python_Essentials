"""
Functions are reusable blocks of code that perform specific tasks.
They help make code more modular, organized, and easier to maintain.

Syntax:
    def function_name(parameters):
        return result

Note:
    A function will only run when it is *called*.
    If you don't call it, it won’t execute.
"""

# 1. Function without parameters
def greet():
    print("Hey hello, this is a function return statement!")

# Function call
greet()

# 2. Function with parameters
def add(a, b):  # formal arguments
    return a + b

print(add(100, 43))  # actual arguments

def sub(a, b):
    return a - b

print(sub(20, 9))  # Output: 11

def mul(a, b):
    return a * b

print(mul(2, 1))

def div(a, b):
    return a / b

print(div(10, 2))

def power(a, b):
    return a ** b

print(power(2, 2))  # 2^2 = 4

def check(a, b):
    return a + b

print(check(a=10, b=5))

# 3. Default arguments
def default(a=29, b=12):
    return a + b

print(default())          # Uses default values → 29 + 12 = 41
print(default(10))        # Overrides 'a' → 10 + 12 = 22
print(default(10, 5))     # Overrides both → 10 + 5 = 15

# 4. Positional arguments using *args
def pos(*names):
    for name in names:
        print("Hey", name)

pos("Prasad", "Hi", "Hey")

# 5. Keyword arguments using **kwargs
def kwfun(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

kwfun(name="prasad", role="Data Analyst", open_to="Freelance")
