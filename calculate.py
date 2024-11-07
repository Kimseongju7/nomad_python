def plus(a = 0, b = 0):
    print(a + b)
def sub(a = 0, b = 0):
    print(a - b)
def mul(a = 0, b = 0):
    print(a * b)
def div(a = 0, b = 1):
    print(a / b)
def div_int(a = 0, b = 1):
    print(a // b)
def mod(a = 0, b = 1):
    print(a % b)
def pow(a = 0, b = 0):
    print(a ** b)

def calculate(a = 0, b = 0):
    plus(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
    div_int(a, b)
    mod(a, b)
    pow(a, b)

a = int(input())
b = int(input())
calculate(a, b)