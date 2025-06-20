# poject

import random

print("Rock, Paper, Sissors game!")
while True:
 while True:
  choice = int(input("Make your choice:\n1 - Rock\n2 - Paper\n3 - sissors\n"))
  bot_choice = random.randint(1, 3)
  if choice > 3:
   print("Please input a valid choice")
   continue
  if (bot_choice == 1 and choice == 2) or (bot_choice == 2 and choice == 3) or (bot_choice == 3 and choice == 1):
   print("You win!")
  elif bot_choice == int(choice):
   print("Its a tie!")
  else:
   print("You lose")
  continue