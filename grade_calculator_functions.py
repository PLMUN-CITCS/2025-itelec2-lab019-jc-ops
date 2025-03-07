def get_student_score():

    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


score = get_student_score()
grade = calculate_grade(score)
print(f"Your Grade is: {grade}")
