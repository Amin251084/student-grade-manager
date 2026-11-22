from Student import *

subjects = ["Math","Physics","Chemistry","English","Computer Science"]
subjects_score = {}

print("========= Welcome =========")
student_name = input("Enter your name: ")

for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter the {subject} score: "))

            if 0 <= score <= 20:
                subjects_score[subject] = score
                break
            else:
                print("Invalid score! Enter a number between 0 and 20.")

        except ValueError:
            print("Invalid input! Please enter a number.")

average = avg(subjects_score)
highest_grade = max_grades(subjects_score)
lowest_grade = min_grades(subjects_score)
term_status = status(average)

print("========== Resault ==========")
print(f"Student name: {student_name}")
print(f"Student average: {average:.2f}")
print(f"Highest_grade: {highest_grade:.2f}")
print(f"Lowest_grade: {lowest_grade:.2f}")
print(f"Term status: {term_status}")