accounts = {
    "12345678": {"pin": 1234, "balance": 1200.0, "history": []},
    "09090909": {"pin": 1919, "balance": 250.0, "history": []}
}

def authenticate_user():
    account_number = input("Please enter your 8-digit account number: ")
    if account_number in accounts:
        trials = 3
        while trials > 0:
            try:
                pin = int(input(f"Enter your 4-digit PIN ({trials} attempts left): "))
                if pin == accounts[account_number]["pin"]:
                    print("\nLogin successful!")
                    return account_number
                else:
                    trials -= 1
                    print("Incorrect PIN. Try again.")
            except ValueError:
                print("Invalid input. Please enter a 4-digit number.")
    else:
        print("Account not found.")
    return None

def display_menu():
    print("\n=== AafaqBank ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    print(f"\nYour current balance is: £{balance:.2f}")

def deposit_money(account_number):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            accounts[account_number]["balance"] += amount
            accounts[account_number]["history"].append(f"Deposited: £{amount:.2f}")
            print(f"£{amount:.2f} has been deposited into your account.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def withdraw_money(account_number):
    """Handles withdrawing money from the user's account."""
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            accounts[account_number]["history"].append(f"Withdrawn: £{amount:.2f}")
            print(f"£{amount:.2f} has been withdrawn from your account.")
        elif amount > accounts[account_number]["balance"]:
            print("Insufficient funds.")
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_transaction_history(account_number):
    history = accounts[account_number]["history"]
    if history:
        print("\nTransaction History:")
        for transaction in history:
            print(transaction)
    else:
        print("\nNo transactions found.")

def atm_session(account_number):
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            deposit_money(account_number)
        elif choice == "3":
            withdraw_money(account_number)
        elif choice == "4":
            view_transaction_history(account_number)
        elif choice == "5":
            print("Thank you for using AafaqBank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("\nWelcome to AafaqBank ATM!")
    while True:
        account_number = authenticate_user()
        if account_number:
            atm_session(account_number)
        else:
            print("\nAuthentication failed. Returning to main menu.")
        
        restart = input("\nWould you like to try another account? (Y/N): ").upper()
        if restart != "Y":
            print("Thank you for using AafaqBank. Goodbye!")
            break

if __name__ == "__main__":
    main()
