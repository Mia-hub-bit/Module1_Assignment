# Initialize a dictionary with student names and their grades.
student_grades = {
    "Mary": [85, 90, 78],
    "Amar": [92, 88, 95],
    "Shelby": [75, 80, 82],
    "Maura": [65, 70, 72],
    "Jared": [95, 98, 100]
}

# --- Calculate Average Grades ---
student_averages = {}
for name, grades in student_grades.items():
    student_averages[name] = sum(grades) / len(grades)

# --- Determine Letter Grades ---
student_letter_grades = {}
for name, average in student_averages.items():
    if 90 <= average <= 100:
        student_letter_grades[name] = "A"
    elif 80 <= average < 90:
        student_letter_grades[name] = "B"
    elif 70 <= average < 80:
        student_letter_grades[name] = "C"
    elif 60 <= average < 70:
        student_letter_grades[name] = "D"
    else:
        student_letter_grades[name] = "F"

print("Student Averages:")
for name, average in student_averages.items():
    print(f"  {name}: {average:.2f}")

print("\nStudent Letter Grades:")
for name, letter in student_letter_grades.items():
    print(f"  {name}: {letter}")

# --- Find the Top Performer ---
top_student = max(student_averages, key=student_averages.get)
top_average = student_averages[top_student]
print(f"\nTop Performer: {top_student} with an average of {top_average:.2f}")

# --- Calculate and Display Class Statistics ---
class_average = sum(student_averages.values()) / len(student_averages)
passing_students = 0
for letter in student_letter_grades.values():
    if letter in ["A", "B", "C"]:
        passing_students += 1

print(f"\nOverall Class Average: {class_average:.2f}")
print(f"Number of Students with a Passing Grade (C or better): {passing_students}")