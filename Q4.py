grade = input("Enter a grade between 4 and 10: ")
grade = float(grade)
if grade < 4 or grade > 10:
    print("Error: Grade must be between 4 and 10")
else:
    if grade == 10:
        letter_grade = "A+"
        performance = "Outstanding"
    elif grade >= 9:
        letter_grade = "A"
        performance = "Excellent"
    elif grade >= 8:
        letter_grade = "B+"
        performance = "Very Good"
    elif grade >= 7:
        letter_grade = "B"
        performance = "Good"
    elif grade >= 6:
        letter_grade = "C+"
        performance = "Average"
    elif grade >= 5:
        letter_grade = "C"
        performance = "Below Average"
    else:
        letter_grade = "D"
        performance = "Poor"
    print(f"Letter Grade: {letter_grade}")
    print(f"Performance: {performance}")
