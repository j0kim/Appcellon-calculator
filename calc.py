
prompt = "Enter two numbers to perform basic arithmetic: "
print(prompt)
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def division(num1, num2):
    return num1/num2

def multiplication(num1, num2):
    return num1*num2

print(addition(num1, num2))
print(subtraction(num1, num2))
print(division(num1, num2))
print(multiplication(num1, num2))