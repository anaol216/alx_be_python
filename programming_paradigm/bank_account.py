class BankAccount:
    def __init__(self, account_number: str, account_balance: float = 0.0):
        self.account_number = account_number
        self.balance = account_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def display_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Current Balance: ${self.balance:.2f}"