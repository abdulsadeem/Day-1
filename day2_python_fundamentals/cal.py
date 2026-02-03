
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

op = input("Enter operator: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")
