#This project takes all of your expenses you have and subtracts them from your intial buf=dget to make budget planning easier on yourself!!
#Date- 10/2/2023
#CTI -110 P1HW2- Travel Expense
#Landon Smith
print("This program calculates and displays travel expenses")
budget = int(input("Please enter your budget:"))
Destination = input("Please enter your travel destination:")
gas = int(input("Please enter how much you will spend on gas:"))
Accommodations = int(input("Please enter how much you will spend on accommodations:"))
Food = int(input("Please enter how much you will spend on food:"))
total = gas + Accommodations + Food 
remaining = budget - total

#print ("THE TOTAL IS:",total)
print('''        Travel Expenses        ''')
print("Location:", Destination)
print("Intial budget:", budget)
print()
print("Fuel:", gas)
print("Accommodations:", Accommodations)
print("Food:", Food)
print()
print("Remaining Balance:",remaining)


