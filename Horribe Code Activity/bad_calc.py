"""
Calculator w/ bad coding practices
Author: Tristan Coleman
"""

# global variables
x = 0
y = 0
res = 0


# violates single responsibility and clean code by doing multiple parts in one function
# and having overly broad except statements
def add():
    global res
    # duplicate input handling which violates DRY
    try:
        val1 = float(input("Enter first number: "))
    except:
        val1 = 0
    try:
        val2 = float(input("Enter second number: "))
    except:
        val2 = 0
    res = val1 + val2
    # doing I/O inside the math function
    print("Result is: " + str(res))


def subtract():
    global res
    # repeated input block (violates DRY)
    try:
        val1 = float(input("Enter first number: "))
    except:
        val1 = 0
    try:
        val2 = float(input("Enter second number: "))
    except:
        val2 = 0
    res = val1 - val2
    print("Result is: " + str(res))


def multiply():
    global res
    # repeated input block (violates DRY)
    try:
        val1 = float(input("Enter first number: "))
    except:
        val1 = 0
    try:
        val2 = float(input("Enter second number: "))
    except:
        val2 = 0
    # bad error handling, crashes or returns string inconsistently
    res = val1 * val2
    print("Result is: " + str(res))


# suboptimal name, mixed responsibilities violating single responsibility
def run():
    c = input("Type add, sub, or div: ")
    if c == "add":
        add()
    elif c == "sub":
        subtract()
    elif c == "div":
        multiply()
    else:
        print("unknown")


run()