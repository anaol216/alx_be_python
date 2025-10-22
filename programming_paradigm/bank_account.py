class BankAccount:
    """
    Represents a simple bank account with basic deposit, withdrawal, 
    and balance display functionality.
    """
    def __init__(self, initial_balance=0.0):
        """Initializes the account with a balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account and prints the result."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        
        self.balance += amount
        # Prints message with one decimal place
        print(f"Deposited: ${amount:.1f}")
        return True

    def withdraw(self, amount):
        """
        Withdraws the specified amount or prints "Insufficient funds."
        Prints the success or failure message directly to stdout.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self.balance:
            # Prints the required error message
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            # Prints success message with one decimal place
            print(f"Withdrew: ${amount:.1f}")
            return True

    def display_balance(self):
        """
        Displays the current balance with two decimal places (e.g., $250.00).
        """
        print(f"Current Balance: ${self.balance:.2f}")