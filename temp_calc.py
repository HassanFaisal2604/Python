list1 = []
n = int(input("How many days temp : "))
i = 0
while i < n:
    input1 = float(input("Enter temperature: "))
    list1.append(input1)
    i += 1
avg_temp = sum(list1) / len(list1)
print("The avg Temperature is", avg_temp)
above_avg_count = 0
for temp in list1:
    if temp > avg_temp:
        print(temp, "is greater than the avg temp")
        above_avg_count += 1
if above_avg_count == 0:
    print("All elements are smaller than or equal to the avg temp")
