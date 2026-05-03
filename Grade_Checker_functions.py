
# Grade Checker: Single file broken into smaller functions

# Input function
def get_score():
    while True:
        try:
            score = float(input("Enter your score (0 - 100): "))
            return score
        except ValueError:
            print("Invalid input! Please enter a number.")

# validity of input
def is_valid_score(score):
    return 0 <= score <= 100

# Conditionals for the score
def compute_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

# Remarks function
def get_remarks(grade):
    remarks = {
        "A": "Excellent!",
        "B": "Very Good",
        "C": "Good",
        "D": "Pass",
        "E": "Poor Pass",
        "F": "Fail"
    }
    return remarks[grade]

# Output function
def display_result(score, grade, remarks):
    print("                            ")
    print("        GRADE REPORT       ")
    print("                              ")
    print(f" Score  : {score}")
    print(f" Grade  : {grade}")
    print(f" Remark : {remarks}")
    print("                            ")

# Main function to direct the flow
def main():
    score = get_score()

    if not is_valid_score(score):
        print("Error: Score must be between 0 and 100.")
        return

    grade = compute_grade(score)
    remarks = get_remarks(grade)
    display_result(score, grade, remarks)


if __name__ == "__main__":
    main()