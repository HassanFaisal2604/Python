class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = float(initial_balance)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance:.2f}"
        return "Invalid deposit amount. Please enter a positive number."
  
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrawal successful. New balance: {self.balance:.2f}"
            return "Insufficient funds."
        return "Invalid withdrawal amount. Please enter a positive number."
     
    def show_balance(self):
        return f"Current balance: {self.balance:.2f}"

accounts = {}

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        option = input("Enter the desired option: ").strip()
        
        if option == "1":
            acc_num = input("Enter your new account number: ").strip()
            if acc_num in accounts:
                print("This account number already exists.")
            else:
                initial_balance = get_float_input("Enter your initial balance: ")
                accounts[acc_num] = BankAccount(acc_num, initial_balance)
                print("Account created successfully!")
            
        elif option == "2":
            acc_num = input("Enter your account number: ").strip()
            if acc_num in accounts:
                dep_amount = get_float_input("Enter the amount you want to deposit: ")
                print(accounts[acc_num].deposit(dep_amount))
            else:
                print(f"Account {acc_num} does not exist.")
                
        elif option == "3":
            acc_num = input("Enter your account number: ").strip()
            if acc_num in accounts:
                withd_amount = get_float_input("Enter the amount you want to withdraw: ")
                print(accounts[acc_num].withdraw(withd_amount))
            else:
                print(f"Account {acc_num} does not exist.")
                
        elif option == "4":
            acc_num = input("Enter your account number: ").strip()
            if acc_num in accounts:
                print(accounts[acc_num].show_balance())
            else:
                print(f"Account {acc_num} does not exist.")
                
        elif option == "5":
            print("Thanks for using our service!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()