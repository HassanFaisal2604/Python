class Computer():
    def __init__(self,brand,model) :
        self.__brand=brand
        self.__model=model
    
    def get_info(self):
     return self.__brand + self.__model
 
computer=Computer("hP   ","2012")
print(computer.get_info())

  
    
    
    