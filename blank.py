
```python
Class BankAccount:
    Def __init__(self, balance=0):
        Self.balance = balance

    Def deposit(self, amount):
        Self.balance += amount
        Print(f”Deposited ${amount}. Current balance: ${self.balance}”)

    Def withdraw(self, amount):
        If self.balance >= amount:
            Self.balance -= amount
            Print(f”Withdrew ${amount}. Current balance: ${self.balance}”)
        Else:
            Print(“Insufficient funds”)

    Def check_balance(self):
        Print(f”Current balance: ${self.balance}”)


# Main program
If __name__ == “__main__”:
    Account = BankAccount()

    While True:
        Print(“\n1. Deposit”)
        Print(“2. Withdraw”)
        Print(“3. Check Balance”)
        Print(“4. Exit”)

        Choice = input(“Enter choice: “)

        If choice == ‘1’:
            Amount = float(input(“Enter deposit amount: “))
            Account.deposit(amount)
        Elif choice == ‘2’:
            Amount = float(input(“Enter withdrawal amount: “))
            Account.withdraw(amount)
        Elif choice == ‘3’:
            Account.check_balance()
        Elif choice == ‘4’:
            Break
        Else:
            Print(“Invalid choice. Please try again.”)
```
