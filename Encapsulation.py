class Bankacount:
    def __init__(self,Balance):
        self.__Balance=Balance
    def depost (self,amount):
        self.__Balance=amount
    def get_balance(self):
        return self.__Balance
account=Bankacount(100)
account.depost(1044)
print(account.get_balance())   

       
        
        
                 
    