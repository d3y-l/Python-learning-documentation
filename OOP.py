# OOP (Object oriented programing)
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return print("Please enter a number.")
class BankAccount:
    def __init__ (self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
    def deposit(self, ammount):
        if is_number(ammount):
            ammount = float(ammount)
            if ammount > 0:
             self.balance += ammount
             self.transactions.append(f"Deposited £{ammount}.")
            return print(f"Deposited £{ammount}. New balance £{self.balance}")
        else:
         return print("Deposit must be positive.")
    def widthdraw(self, ammount):
        if is_number(ammount):
            ammount = float(ammount)
            if ammount > 0:
             self.balance -= ammount
             self.transactions.append(f"Widthdew £{ammount}.")
             return print(f"Widthdrew £{ammount}. New balance £{self.balance}")
            elif ammount > self.balance:
             return print("Insufficient funds.")
        else:
         return print("Widthdrawal must be positive.")
    def get_bal(self):
        return print(f"You have £{self.balance}.")
    def get_transaction_hist(self):
        return print(self.transactions)
    def pay(self, recipient, ammount):
        if is_number(ammount):
            ammount = float(ammount)
        else:
            print("Please enter a number.")
        if not isinstance(recipient, BankAccount):
         return print("Recipient must be a bank account object.")
        if ammount <= 0:
          return print("Payment must be positive.")
        elif ammount > self.balance:
          return print("Insufficient funds.")
        else:
            self.balance -= ammount
            recipient.balance += ammount
            self.transactions.append(f"Paid {recipient.name}, £{ammount}.")
            recipient.transactions.append(f"Recived £{ammount} from {self.name}.")
            return print(f"Paid {recipient.name}, £{ammount}.")
        
print("Python bank!")
print("Please create an account.\nPlease type your name below.")
acc1 = BankAccount(input())
bob = BankAccount("bob", 100)
while True:
 print("Please select an option.\n1. Deposit money\n2. Withdraw money\n3. Get your balance\n4. Get your transaction history\n5. pay another person")
 choice = input()
 if choice == "1":
    acc1.deposit(input("Please enter the amount you would like to deposit.\n"))
    continue
 elif choice == "2":
    acc1.widthdraw(input("Please enter the amount you would like to withdraw.\n"))
    continue
 elif choice == "3":
    acc1.get_bal()
    continue
 elif choice == "4":
    acc1.get_transaction_hist()
    continue
 elif choice == "5":
    acc1.pay(BankAccount(input("Please enter the person you would like to pay.\n")), input("Please enter how much you would like to pay.\n"))
    continue
 else:
    print("Please enter a valid number.")
    continue