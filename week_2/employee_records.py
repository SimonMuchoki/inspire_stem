#get employee name full name , salary , bonuses, inc employees salary by 30% , decrease bonus by 5000

import math

first_name = (input("Enter your first name :"))
second_name =(input("Enter your second name :"))

print(first_name +" " + second_name)

salary = float(input("Enter your salary ksh :"))

bonuses = float(input("employee bonuses :"))

new_salary = salary * (30/100)
new_bonuses = bonuses - 5000

print("Employee's new salary : ksh",new_salary)
print("Employee's new bonuses : ksh",new_bonuses)
