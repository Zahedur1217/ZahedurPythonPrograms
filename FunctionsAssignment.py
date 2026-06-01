# -----------------------------------
# Employee List (Up to 5 Employees)
# -----------------------------------

employees = []

# -----------------------------------
# Get Employee ID
# -----------------------------------
def get_employee_id():
    while True:
        emp_id = input("Enter Employee ID (7 digits or less): ")

        if emp_id.isdigit() and len(emp_id) <= 7:
            return emp_id

        print("Invalid ID. Try again.")


# -----------------------------------
# Get Employee Name
# -----------------------------------
def get_employee_name():
    while True:
        name = input("Enter Employee Name: ")

        invalid_chars = "!\"@#$%^&*()_=+,<>/?;:[]{}\\"

        if all(char.isalpha() or char.isspace() for char in name):
            if not any(char in name for char in invalid_chars):
                return name

        print("Invalid name. Try again.")


# -----------------------------------
# Get Employee Email
# -----------------------------------
def get_employee_email():
    while True:
        email = input("Enter Employee Email: ")

        invalid_chars = "!\"'#%^&*()=+,<>/?;:[]{}\\"

        if not any(char in email for char in invalid_chars):
            return email

        print("Invalid email. Try again.")


# -----------------------------------
# Get Employee Address (optional)
# -----------------------------------
def get_employee_address():
    while True:
        address = input("Enter Employee Address (optional): ")

        if address == "":
            return ""

        invalid_chars = "!\"'@%^&*_+=<>?;:[]{}"

        if not any(char in address for char in invalid_chars):
            return address

        print("Invalid address. Try again.")


# -----------------------------------
# Collect employees (up to 5)
# -----------------------------------
for i in range(5):
    print("\nEnter details for employee", i + 1)

    employee = {
        "id": get_employee_id(),
        "name": get_employee_name(),
        "email": get_employee_email(),
        "address": get_employee_address()
    }

    employees.append(employee)


# -----------------------------------
# Print final list
# -----------------------------------
print("\nAll Employees:")
print(employees)