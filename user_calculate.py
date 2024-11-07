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

while True:
    a = int(input("Choose a number: "))
    b = int(input("Choose another one: "))
    print("Choose an operation: ")
    print("\tOptions are: +, -, *, or /.")
    print("Write 'exit' to finish.")
    operation = input()
    if(operation == "exit") :
        break
    elif operation == "+":
        plus(a, b)
    elif operation == "-":
        sub(a, b)
    elif operation == "*":
        mul(a, b)
    elif operation == "/":
        div(a, b)
    else :
        print(f"Unknown operation: {operation}")
