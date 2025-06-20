# learning code
print("Hello World")
mystring = 'It\'s me!'
print(mystring)
string2 = 'a'
string3 = 'b'
print(string2 + string3)
print(string2 * 3)
string4 = "testng \"escaping\""
print(string4)
User_input = input("Please enter your name.\n") 
print("Hello, "+ User_input +"!")
if User_input == "Gilbert":
 print("You made this program!")
else:
 print("Who are you!\n \n \n \n")




# Calculator code
print('Python calculator!')
n1 = input("Please enter your first number:\n\n")
n2 = input("Please enter your second number:\n\n")
# Ask for thrid number
q1 = input("Do you want to enter more numbers? (Yes or No)\n\n")
# Get thrid number
if q1 == "yes" or q1 == "Yes":
 n3 = input("Please enter your thrid number:\n\n")
 # Ask for fourth number
 q2 = input("Do you want to enter more numbers? (Yes or No)\n\n")
 if q2 == "yes" or q2 == "Yes":
   print("This calculator only accepts 3 numbers.\n\n")
 else:
   print("Great! On to step 2.\n\n\n")
   q4 = input("Please type 1 for addition\nPlease type 2 for subtraction\nPlease type 3 for multiplication\nPlease type 4 for division\n\n")
   if q4 == "1":
    print("Answer is: "+ n1 + n2 + n3)
   elif q4 == "2":
    print("Answer is: "+ n1 - n2 - n3)
   elif q4 == "3":
    print("Answer is: "+ n1 * n2 * n3)
   elif q4 == "4":
    print("Answer is: "+ n1/n2/n3)
    print("\n\nCalculation complete!")
else:
 print("Great! On to step 2.\n\n\n")

q3 = input("Please type 1 for addition\nPlease type 2 for subtraction\nPlease type 3 for multiplication\nPlease type 4 for division\n\n")
if q3 == "1":
 print("Answer is: "+ n1 + n2)
elif q3 == "2":
 print("Answer is: "+ n1 - n2)
elif q3 == "3":
 print("Answer is: "+ n1 * n2)
elif q3 == "4":
 print("Answer is: "+ n1/n2)
print("\n\nCalculation complete!")





# calculator attemt 2
def add(x, y):
 return(x + y)
def subtract(x, y):
 return(x-y)
def divide(x, y):
 return(x/y)
def multiply(x, y):
 return(x*y)
while True:
 print('1. Addition\n2. Subtraction\n3. Division\n4. Multiplication')
 choice = input('Please select an option (1, 2, 3, 4)\n')
 if choice in ('1', '2', '3', '4'):
  try:
   num1 = float(input("Please enter your first number"))
   num2 = float(input("Please enter your second numeber"))
  except ValueError:
   print("Please enter a valid number")
  continue
 if choice == "1":
  print(num1, "+", num2, "=", add(num1, num2))
 elif choice == "2":
  print(num1, "-", num2, "=", subtract(num1, num2))
 elif choice == "3":
  print(num1, "/", num2, "=", divide(num1, num2))
 elif choice == "4":
  print(num1, "*", num2, "=", multiply(num1, num2))
  choice2 = input('Would you like to do another calculation? (y/n)')
  try:
   if choice2 in ('yes', 'y', 'Yes', 'Y'):
    continue
   elif choice2 in ('n', 'N', 'no', 'No'):
    break
  except:
   print("Please enter a valid answer")