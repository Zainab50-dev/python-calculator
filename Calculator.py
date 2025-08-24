print("Welcome to Calculator!")

def addition(num1,num2):
    return (num1 + num2)
def subtraction(num1,num2):
    return (num1 - num2)
def multiplication(num1,num2):
    return (num1 * num2)
def division(num1,num2):
     return (num1 / num2)
def exponent(num1,num2):
     return (num1 ** num2)
def modulus(num1,num2):
     return (num1 % num2)

while True:
     num1 = (input("Enter first number(or type exit to quit):"))
     if num1 == "exit":
          break
     try:
          num1 = float(num1)
     except ValueError:
          print("The input should be float value!")
          continue
     
     operator = input("Enter the operation you want to perform(+,-,*,/):")
     num2 = input("Enter second number:")
     try:
          num2 = float(num2)
     except ValueError:
          print("The input should be float value!")
          continue
     
     if operator == "+":
          print("Result:",addition(num1,num2))
     elif operator == "-":
          print("Result:",subtraction(num1,num2))
     elif operator == "*":
          print("Result:",multiplication(num1,num2))
     elif operator == "/":
          try:
               print("Result:",division(num1,num2))
          except ZeroDivisionError:
               print("Sorry cannot divide by 0")       
     elif operator == "**":
          print("Result:",exponent(num1,num2)) 
     elif operator == "%":
          print("Result:",modulus(num1,num2))
     else:
          print("Invalid operator!")
        

 



 


