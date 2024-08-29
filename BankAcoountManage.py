class BankAccount():
    def __init__(self,Account_number,initial_balance=0):
        
        self.Account_number=Account_number
        self.initial_balance=initial_balance  #First have to create an account number. then ask for initial balance
        
    
    
    def deposit(self , amount):
      self.balance+=amount
      return self.balance
  
    def withdraw(self,amount):
     if amount <= self.balance:
         return self.balance
     else: 
         return "The balance is insufficent" 
     
    def show(self):
     return self.balance  
Accounts={}
while True:
    print("Enter the desired option: ")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
     

   
    