team=input("Select Team 1, Team 2 or Team 3.")
if team == "Team 1":
    print("You picked team 1, which has 1 character, which is Yoda")
elif team == "Team 2":
    print("You picked team 2, which has 2 characters, Jack & Rose")
elif team ==   "Team 3":
    print("You picked team 3, which has 2 characters, Vader & Leah")
else:
    print("Please only Select Team 1, Team 2 or Team 3 ")
if team == "Team 1" or "Team 3":
    print("The number of people on the team you selected is odd." )
else:
    print("The number of people on the team you selected is even.")    