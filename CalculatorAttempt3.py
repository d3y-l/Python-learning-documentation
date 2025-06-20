# calculator attempt 3
import random
def add(x, y):
    return(x + y)
def subtract(x, y):
    return(x - y)
def multiply(x, y):
    return(x*y)
def divide(x, y):
    return(x/y)
def is_valid_number(x):
  try:
    float(x)
    return True
  except ValueError:
    return False

while True:
 print("Python calculator 3.0!")
 while True:
     print("Please input your calculation below using * for multiply and / for divide.\n")
     num1 = input()
     if is_valid_number(num1):
       num1_int = float(num1)
       print(num1_int)
     else:
      print("Please enter a number.")
      continue
     break
 while True:
    choice1 = input()
    if choice1 in ("+", "-", "*", "/"):
     print(num1_int, choice1)
     break
    else:
     print("Please enter either \"+\", \"-\", \"*\" or \"/\".")
    continue 
 while True:
  num2 = input()
  if is_valid_number(num2):
   num2_int = float(num2)
   print(num1_int, choice1, num2_int, "=")
   break
  else:
   print("Please enter a number.")
  continue
 if choice1 == "+":
  print(add(num1_int, num2_int))
 elif choice1 == "-":
  print(subtract(num1_int, num2_int))
 elif choice1 == "*":
  print(multiply(num1_int, num2_int))
 elif choice1 == "/":
  print(divide(num1_int, num2_int))
 again = input("Do you want to do another calculation? (y/n)")
 if again in ("yes", "y", "Yes", "Y"):
  continue
 else:
   break