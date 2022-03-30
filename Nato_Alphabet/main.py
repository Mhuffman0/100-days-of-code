import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

student_scores = {student: random.randint(0, 100) for student in names}
print(student_scores)

passed_students = {
    student: score
    for (student, score) in student_scores.items()
    if score > 59
}

print(passed_students)
