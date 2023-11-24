# CTI-110
# P4HW2 - Salary Calculato
# Landon Smith
# Date 11/24/2023

overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0
#start of loop
while True:
    
    employee_name = input("Enter employee name (or 'Done' to finish): ")
    
#conditon to break loop    
    if employee_name.lower() == 'done':
        break

    
    num_employees += 1

    
    
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter employee pay rate: "))
    
    overtime_hours = max(hours_worked - 40, 0)
    overtime_pay = 0
#calculates overtime pay 
    if overtime_hours > 0:
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        overtime_total += overtime_pay

#calculates regular pay
    regular_hours = hours_worked - overtime_hours
    regular_pay = regular_hours * pay_rate
    regular_pay_total += regular_pay

 #calculates total pay   
    total_pay = regular_pay + overtime_pay
    gross_pay_total += total_pay

#prints only the employee info for each individual employee
    print("\nEmployee Information:")
    print("Employee Name:", employee_name)
    print("Pay Rate: $", format(pay_rate, ".2f"))
    print("Number of Hours Worked:", hours_worked)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay: $", format(overtime_pay, ".2f"))
    print("Regular Hours:", regular_hours)
    print("Regular Pay: $", format(regular_pay, ".2f"))
    print("Gross Pay: $", format(total_pay, ".2f"))
#Prints the total info gathered in the loop.
print("Number of Employees: ", num_employees)
print("\nTotal Information:")
print("Total Overtime Pay: $", format(overtime_total, ".2f"))
print("Total Regular Pay: $", format(regular_pay_total, ".2f"))
print("Total Gross Pay: $", format(gross_pay_total, ".2f"))


















