import random

# Employee names and departments
employees = ["Alice", "Bob", "Charlie", "David", "Emma"]
departments = ["Sales", "Engineering", "HR", "Marketing"]

# Generate random performance scores (for 6 months)
performance_data = {
    emp: {f"Month {m+1}": random.randint(50, 100) for m in range(6)}
    for emp in employees
}

# Employee performance report
report = {}

# Process each employee
for emp, scores in performance_data.items():
    total_score = 0
    num_months = len(scores)

    # Loop through months and sum scores
    for month, score in scores.items():
        total_score += score

    # Calculate the average score
    avg_score = total_score / num_months

    # Assign a performance level
    if avg_score >= 90:
        level = "Outstanding"
    elif avg_score >= 80:
        level = "Excellent"
    elif avg_score >= 70:
        level = "Good"
    elif avg_score >= 60:
        level = "Needs Improvement"
    else:
        level = "Poor"

    # Assign employee to a random department
    department = random.choice(departments)

    # Store report data
    report[emp] = {
        "Department": department,
        "Average Score": round(avg_score, 2),
        "Performance Level": level
    }

# Write results to a file
with open("employee_performance.txt", "w") as file:
    file.write("Employee Performance Report\n")
    file.write("="*40 + "\n")
    
    for emp, details in report.items():
        file.write(f"{emp} ({details['Department']}): Avg Score = {details['Average Score']}, Level = {details['Performance Level']}\n")

# Display report
for emp, details in report.items():
    print(f"{emp} ({details['Department']}): Avg Score = {details['Average Score']}, Level = {details['Performance Level']}")
