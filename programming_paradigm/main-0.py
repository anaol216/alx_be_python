from programming_paradigm.bank_account import BankAccount

def main():
    # Set an initial balance high enough to allow the first withdrawal test ($50.0)
    print("--- Setup: Initializing Account with $100.00 ---")
    account = BankAccount(100.00)
    account.display_balance()

    # --- Test 1: Deposit (Example $67.0) ---
    print("\n--- Test: Deposit $67.0 ---")
    # This call must only happen ONCE
    account.deposit(67.0) 
    
    # Balance should now be $167.00
    account.display_balance()

    # --- Test 2: Withdrawal (Example $50.0) ---
    print("\n--- Test: Successful Withdrawal of $50.0 ---")
    # This call must only happen ONCE
    account.withdraw(50.0)
    
    # Balance should now be $117.00
    account.display_balance()

    # --- Test 3: Withdraw More Than You Have (Example $300.0) ---
    print("\n--- Test: Withdrawal of $300.0 (Insufficient Funds) ---")
    # This call must only happen ONCE
    account.withdraw(300.0)
    
    # Balance should still be $117.00
    account.display_balance()


if __name__ == "__main__":
    main()