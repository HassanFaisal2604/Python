first_class=int(870)
second_class=int(100.42)
third_class=int(7)
ticket="How many 1st, 2nd and 3rd class tickets do you want to purchase?"
first=int(input("First class ="))
second=int(input("Second class ="))
third=int(input("third class ="))
total_ticket=int((first_class*first)+(second_class*second)+(third_class*third))
print(f"The Total price is {total_ticket:.2f} $")