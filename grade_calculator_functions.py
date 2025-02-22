def get_student_score():
    """Gets the student's score as a number."""
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_grade(score):
    """Returns the letter grade based on the grading scale."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program
if __name__ == "__main__":
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")
