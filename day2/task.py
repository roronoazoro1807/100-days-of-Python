print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total=1+(tip/100)
total_per_person=(bill/people)*total
formatting_total=round(total_per_person,2)

print(f"each person should pay :{formatting_total}")


