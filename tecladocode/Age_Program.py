# Write a program that asks the user for their age
# and tells them their age in seconds.

# Optionally, extend the program so it prints months,
# days, hours, and seconds.

user_age = input("Enter your age: ")
years = int(user_age)
months = years * 12
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"That's {months} months.")
print(f"Or {days} days.")
print(f"Or {hours} hours.")
print(f"Or {minutes} minutes.")
print(f"Or {seconds} seconds.")