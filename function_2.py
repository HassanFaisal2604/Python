name=input("Who was on titanic when it sunk")
year=int(input("What year is it today"))
def titanic(name,year):
    
    year_Passed=year-1912
    print(f" {name}  were on titanic when it sunk",year_Passed," years ago")
titanic(name,year)
    