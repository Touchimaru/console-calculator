#A simple calculator program

print("Calculator this are the operators ")

#operators

print("1 for addition")
print(" 2 for subtraction")
print(" 3 for multiplication")
print(" 4 for division")

#op input
op  = input("Enter your operator: ")

#numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


#if statement aka the computation process

if op == "1":
  print("The answer is ", num1 + num2)

if op == "2":
  print("The answer is ", num1 - num2)

if op == "3":
  print("The answer is ", num1 * num2)

if op == "4":
  print("The answer is ", num1 / num2)
  
#i dont add an else statement because when i add it the program wont work properly so there will be no error and no answer if the operator is incorrect


print("Thank you for using my program  Press enter to exit")
input()
  
