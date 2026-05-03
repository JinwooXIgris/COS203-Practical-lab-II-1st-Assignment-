# LOGIC MODULE: Handles validation and grade computation

# To check for score validity
def is_valid_score(score):
    return 0 <= score <= 100

# Conditional for the score
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