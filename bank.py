# Write a Python program to create a class representing a bank. Include methods for
# managing customer accounts and transactions.


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            self.accounts[account_number] = 1200000  
            print(f"Account {account_number} created successfully with an initial balance of 12 lakh")
        else:
            print(f"Account {account_number} already exists!")

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} into account {account_number}. Current balance is {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} does not exist!")

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}. Current balance is {self.accounts[account_number]}")
            else:
                print(f"Insufficient funds in account {account_number}!")
        else:
            print(f"Account {account_number} does not exist!")

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print(f"Balance in account {account_number} is {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} does not exist!")


bank = Bank()

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.deposit()
    elif choice == '3':
        bank.withdraw()
    elif choice == '4':
        bank.check_balance()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
