import random

# Sample student data
students = ["Alice", "Bob", "Charlie", "David", "Emma"]
subjects = ["Math", "Science", "History", "English", "Art"]

# Generate random scores for each student in each subject
scores = {student: {subject: random.randint(50, 100) for subject in subjects} for student in students}

# Compute the average scores and grade classifications
report = {}
for student, subject_scores in scores.items():
    total_score = 0
    subject_count = len(subject_scores)

    for subject, score in subject_scores.items():
        total_score += score

    average_score = total_score / subject_count

    # Grade classification
    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    report[student] = {"Average Score": round(average_score, 2), "Grade": grade}

# Display the results
print("Student Report:")
for student, details in report.items():
    print(f"{student}: Avg Score = {details['Average Score']}, Grade = {details['Grade']}")
