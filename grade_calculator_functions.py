"""Obtains student score and gives corresponding grade."""
def get_student_score():
    """Prompts user for student score and returns it."""
    sscore = int(input("Enter your score: "))
    return sscore

def calculate_grades(ssscore):
    """Returns the grade corresponding to the student score."""
    if ssscore >= 90:
        grade = "A"
    elif ssscore >= 80:
        grade = "B"
    elif ssscore >= 70:
        grade = "C"
    elif ssscore >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

if __name__ == "__main__":
    score = get_student_score()
    GRADE = calculate_grades(score)
    print(f"Your Grade is: {GRADE}")
