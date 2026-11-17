class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")
    def display(self):
        print("Account Holder:", self.name)
        print("Balance: Rs.", self.balance)
# Create account
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")

    print("3. Balance Enquiry")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.display()
    elif choice == "4":
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid choice!")
