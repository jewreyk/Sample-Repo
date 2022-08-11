# Employee Earnings
#
# Input employee name, hours worked, and hourly wage
# Process them appropriately
# Print out

name = input("Please enter your name: ").capitalize().strip()

hours_worked = input("Please enter your hours worked: ")

hourly_wage = input("Please enter your hourly wage: ")

earnings = float(hourly_wage) * float(hours_worked)
print(f"{name} earned ${earnings} this week.")