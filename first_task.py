print("Welcome to Basic Calculator")

num1 = float(input("Enter First number:"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter second number:"))

if operator == "+":
  print("Result :", num1+num2)
elif operator == "-":
  print("Result :", num1-num2)
elif operator == "*":
  print("Result :", num1*num2)
elif operator == "/":
  print("Result :", num1/num2)
else:
  print("Invalid operator")