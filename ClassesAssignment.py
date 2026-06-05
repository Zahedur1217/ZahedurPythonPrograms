# -----------------------------------
# Validator Class
# -----------------------------------

class Validator:

    def validate_name(self, name):
        invalid_chars = '!\"@#$%^&*()_=+,<>/?;:[]{}\\'

        for char in name:
            if char in invalid_chars:
                return False

        return name.replace(" ", "").isalpha()

    def validate_email(self, email):
        invalid_chars = '!\"\'#$%^&*()=+,<>/?;:[]{}\\'

        for char in email:
            if char in invalid_chars:
                return False

        if "@" not in email:
            return False

        return True

    def validate_student_id(self, student_id):
        if not student_id.isdigit():
            return False

        if len(student_id) > 7:
            return False

        return True

    def validate_program(self, program):
        return len(program.strip()) > 0


# -----------------------------------
# Base Class
# -----------------------------------

class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email


# -----------------------------------
# Student Class
# -----------------------------------

class Student(Person):

    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        print("Student")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Student ID:", self.student_id)
        print("Program:", self.program)
        print()


# -----------------------------------
# Main Program
# -----------------------------------

college_records = []

validator = Validator()

while True:

    print()
    print("Enter Student Information")
    print()

    # name validation
    while True:
        name = input("Enter name: ")

        if validator.validate_name(name):
            break

        print("Invalid name. Try again.")

    # email validation
    while True:
        email = input("Enter email: ")

        if validator.validate_email(email):
            break

        print("Invalid email. Try again.")

    # student id validation
    while True:
        student_id = input("Enter Student ID: ")

        if validator.validate_student_id(student_id):
            break

        print("Student ID must be 7 digits or less.")

    # program validation
    while True:
        program = input("Enter Program of Study: ")

        if validator.validate_program(program):
            break

        print("Program of Study is required.")

    # create student object
    student = Student(
        name,
        email,
        student_id,
        program
    )

    college_records.append(student)

    choice = input("Add another student? (yes/no): ")

    if choice.lower() != "yes":
        break


# -----------------------------------
# Display All Records
# -----------------------------------

print()
print("College Records")
print()

for record in college_records:
    record.displayInformation()