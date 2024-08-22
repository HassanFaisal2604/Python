shopping_list = ["Milk", "Eggs","Bread" ,"Banana"]
shopping_list.remove("Bread")
shopping_list.append("Apple")


def show_list(shopping_list):
    for element in shopping_list:
        print(element)

def show_total(shopping_list):
    return len(shopping_list)

print("Here is the shopping list:")
show_list(shopping_list)

print("Here is the total number of items:", show_total(shopping_list))
