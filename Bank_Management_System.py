# Bank Management System

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = {
        "Name": name,
        "Balance": balance
    }

    print("Account created successfully!")

def deposit():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Deposit Amount: "))
        accounts[acc_no]["Balance"] += amount
        print("Amount deposited successfully!")
        print("Current Balance:", accounts[acc_no]["Balance"])
    else:
        print("Account not found!")

def withdraw():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= accounts[acc_no]["Balance"]:
            accounts[acc_no]["Balance"] -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", accounts[acc_no]["Balance"])
        else:
            print("Insufficient Balance!")
    else:
        print("Account not found!")

def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["Name"])
        print("Current Balance:", accounts[acc_no]["Balance"])
    else:
        print("Account not found!")

def view_accounts():
    if len(accounts) == 0:
        print("No accounts available.")
        return

    print("\n===== Account Details =====")
    for acc_no, details in accounts.items():
        print(f"""
Account Number : {acc_no}
Account Holder : {details['Name']}
Balance        : {details['Balance']}
-------------------------------
""")

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        view_accounts()

    elif choice == "6":
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
