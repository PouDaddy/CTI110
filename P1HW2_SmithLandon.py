#This project takes all of your expenses you have and subtracts them from your intial buf=dget to make budget planning easier on yourself!!
#Date- 10/2/2023
#CTI -110 P1HW2- Travel Expense
#Landon Smith
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget:"))
Destination = input("Enter your travel destination:")
gas = float(input("How much do you think you will spend on gas?"))
Accommodations = float(input("Approximately, how much will you need for accomodation/hotel?"))
Food = float(input("Last, how much do you need for food?"))
total = gas + Accommodations + Food 
remaining = budget - total
formatted_budget = f"${budget:.1f}"
formatted_fuel = f"${gas:.1f}"
formatted_accomodation = f"${Accommodations:.1f}"
formatted_food = f"${Food:.1f}"
formatted_balance= f"${remaining:.1f}"
#print ("THE TOTAL IS:",total)
print('''----------Travel Expenses----------''')
print("Location:",Destination)
print("Intial budget:",formatted_budget)
print("Fuel:",formatted_fuel)
print("Accomodations:",formatted_accomodation)
print("Food:",formatted_food)
print("------------------------------------------")
print()
print("Remaining Balance:",formatted_balance)
