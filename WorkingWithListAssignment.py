
# ----------------------------------------
# 1. Create list of courses taken (lowercase)
# ----------------------------------------
courses_taken = [
    "networks and operating systems",
    "principles of software engineering",
    "securing cyber physical systems",
    "system analysis and design"
]

# ----------------------------------------
# 2. Sort list and print with message (uppercase)
# ----------------------------------------
courses_taken.sort()

for course in courses_taken:
    print("I have taken " + course.upper() + " at Walsh College.")

print("\n")

# ----------------------------------------
# 3. Add upcoming courses and re-sort
# ----------------------------------------
courses_taken.extend([
    "cloud computing",
    "data analytics"
])

courses_taken.sort()

print("This is my course of study with upcoming courses added:")
for course in courses_taken:
    print(course)

print("\n")

# ----------------------------------------
# 4. Remove courses already taken and print removed
# ----------------------------------------
print("I do not have to take these courses:")

courses_removed = [
    "networks and operating systems",
    "principles of software engineering"
]

for course in courses_removed:
    if course in courses_taken:
        courses_taken.remove(course)
        print(course.upper())

print("\n")

# ----------------------------------------
# 5. Print remaining courses
# ----------------------------------------
print("I plan to take the following courses next term")
for course in courses_taken:
    print(course)

print("\n")

# ----------------------------------------
# 6. List numbers 1 to 1000 divisible by 6
# ----------------------------------------
div_by_6 = []

for i in range(1, 1001):
    if i % 6 == 0:
        div_by_6.append(i)

# ----------------------------------------
# 7. Print first 20 numbers divisible by 6
# ----------------------------------------
print("Here are twenty numbers divisible by 6.")

for i in range(20):
    print(div_by_6[i])

print("\n")

# ----------------------------------------
# 8. Find maximum value
# ----------------------------------------
max_value = max(div_by_6)

print("The maximum value in the list is: " + str(max_value))

# ----------------------------------------
# 9. Sum values from 10th to 50th item
# ----------------------------------------
sum_values = sum(div_by_6[9:50])

print("Here is the sum of several values in the list: " + str(sum_values))

# ----------------------------------------
# 10. Overwrite course list with number list
# ----------------------------------------
courses_taken = div_by_6