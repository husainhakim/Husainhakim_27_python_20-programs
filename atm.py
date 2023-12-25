class ATM:
    def __init__(self):
        self.balance = 12495
        self.pin_verified = False

    def verify_pin(self, entered_pin):
        stored_pin = "1234"  
        if entered_pin == stored_pin:
            self.pin_verified = True
            return True
        else:
            return False

    def show_balance(self):
        print(f"Your balance is ₹ {self.balance}")

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹ {amount} deposited successfully")
            self.show_balance()
        else:
            print("Amount deposited cannot be negative. Please enter a positive number.")

    def withdraw_money(self, amount):
        if self.pin_verified:
            if amount > 0 and amount <= self.balance:
                print(f"₹ {amount} withdrawn successfully")
                self.balance -= amount
                self.show_balance()
            elif amount > self.balance:
                print("Insufficient funds")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("PIN verification required before withdrawing.")

atm = ATM()

print("Welcome to our ATM menu. Please enter your first name to continue.")
name = input()
print("Please enter your account number to continue.")
account_no = input()

print(f"\nGood day, Mr/Mrs. {name}. Your account number is {account_no}. Please insert your ATM card and do not remove it until you're done with the transaction.")

pin_attempts = 3
while pin_attempts > 0:
    print("Please enter your account PIN number:")
    pin = input()
    if atm.verify_pin(pin):
        break
    else:
        print("Incorrect PIN. Please try again.")
        pin_attempts -= 1

if atm.pin_verified:
    print("\nHow can we help you today?")
    print("1. Show balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input())
    if choice == 1:
        atm.show_balance()
    elif choice == 2:
        amount = int(input("Enter the amount you want to deposit: ₹ "))
        atm.deposit_money(amount)
    elif choice == 3:
        amount = int(input("Enter the amount of money you want to withdraw: ₹ "))
        atm.withdraw_money(amount)
    elif choice == 4:
        print("Exiting the ATM! Have a great day ahead.")
    else:
        print("Invalid choice.")
else:
    print("Too many incorrect attempts. Exiting.")
