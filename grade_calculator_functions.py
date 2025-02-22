def get_student_score():

        score = float(input("Enter your score: "))
        return score


def calculate_grade(sscore):
    if sscore >= 90:
        return 'A'
    elif sscore >= 80:
        return 'B'
    elif sscore >= 70:
        return 'C'
    elif sscore >= 60:
        return 'D'
    else:
        return 'F'

def main():
    ssscore = get_student_score()
    grade = calculate_grade(ssscore)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()