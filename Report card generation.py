# Simple Student Report Card Program

print("===== Student Report Card Generator =====")

# Taking student details
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Taking marks for subjects
print("\nEnter marks out of 100:")
english = float(input("English: "))
math = float(input("Math: "))
science = float(input("Science: "))

# Calculate total and percentage
total = english + math + science
percentage = total / 3

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Print the report card
print("\n===== REPORT CARD =====")
print(f"Name        : {name}")
print(f"Roll Number : {roll}")
print("-----------------------------")
print(f"English : {english}")
print(f"Math    : {math}")
print(f"Science : {science}")
print("-----------------------------")
print(f"Total Marks : {total} / 300")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print("=============================")
