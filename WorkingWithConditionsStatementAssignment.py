# Original employee data list

employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Empty lists

employee_numbers = []
employee_names = []
salary_info = []

# Sorting data into separate lists

for item in employee_data:

    if type(item) == int and item not in employee_numbers:
        employee_numbers.append(item)

    elif type(item) == str and item not in employee_names:
        employee_names.append(item)

    elif type(item) == float and item not in salary_info:
        salary_info.append(item)

# Print the lists

print("Employee Numbers:")
print(employee_numbers)

print()

print("Employee Names:")
print(employee_names)

print()

print("Salary Information:")
print(salary_info)

print()

# Calculate total hourly rates with benefits

total_hourly_rate = []

for salary in salary_info:
    total = salary * 1.3
    total_hourly_rate.append(total)

# Print total hourly rates

print("Total Hourly Rates:")
print(total_hourly_rate)

print()

# Check maximum hourly rate

max_rate = max(total_hourly_rate)

if max_rate > 37.30:
    print("Warning: Someone's salary may be a budget concern.")

print()

# Find underpaid salaries

underpaid_salaries = []

for rate in total_hourly_rate:

    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("Underpaid Salaries:")
print(underpaid_salaries)

print()

# Calculate raises

company_raises = []

for salary in salary_info:

    if salary >= 22 and salary < 24:
        new_salary = salary + (salary * 0.05)

    elif salary >= 24 and salary < 26:
        new_salary = salary + (salary * 0.04)

    elif salary >= 26 and salary < 28:
        new_salary = salary + (salary * 0.03)

    else:
        new_salary = salary + (salary * 0.02)

    company_raises.append(new_salary)

print("Company Raises:")
print(company_raises)

print()

# This condition checks if:
# the employee number exists,
# the employee name exists,
# the salary list has more than 3 values,
# and the highest salary is greater than 25

if 1121 in employee_numbers and "David Toma" in employee_names and len(salary_info) > 3 and max(salary_info) > 25:
    print("The employee data passed the complex condition test.")