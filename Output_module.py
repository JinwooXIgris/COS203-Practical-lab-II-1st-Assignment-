# OUTPUT MODULE: Handles all display/output


def display_result(score, grade, remarks):
    print("                             ")
    print("        GRADE REPORT       ")
    print("                             ")
    print(f" Score  : {score}")
    print(f" Grade  : {grade}")
    print(f" Remark : {remarks}")
    print("                           ")


def display_error(message):
    print(f"Error: {message}")