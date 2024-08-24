menu={'Burger': ('Main', 10.5), 'Soup': ('Appetizer', 5.0),'ice cream': ('Desert',7.0),'Salad':('Health',4.0)}
menu['stake']=('Main',12.5)
menu["Soda"]=("Cold drink",4.5)

def display_menu(menu):
    for keys,val in menu.items():
        print(keys,":",val)
def count_menu(menu):
    val_count={}
    for dish, (category, price) in menu.items():
        if category in val_count:
            val_count[category] += 1  # Increment the count if the category exists
        else:
            val_count[category] = 1  # Initialize the count if the category is not in val_count
    return val_count
def new_price(menu,dish_name,price):
    if dish_name in menu:
        category=menu[dish_name]
        menu[dish_name]=(category,price)
    else:
        print("This dish does not exitst")    
display_menu(menu)
print(count_menu(menu))
new_price(menu,"Soup",1000)
display_menu(menu)