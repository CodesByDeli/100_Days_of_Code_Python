print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_procent = ( tip / 100 ) + 1
#print(tip_procent)
final_count_tip = (bill / people) * tip_procent
#round_final_count_tip = round(final_count_tip,2) > pri pouziti hodnot $150, 12% tip a 5 lidi hazel jedno desetine
formatted_amount = "{:.2f}".format(final_count_tip)
print(f"Each person should pay: {formatted_amount}")