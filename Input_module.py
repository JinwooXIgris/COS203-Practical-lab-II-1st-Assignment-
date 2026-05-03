
# INPUT MODULE: Handles all user input


def get_score():
    while True:
        try:
            score = float(input("Enter your score (0 - 100): "))
            return score
        except ValueError:
            print("Invalid input! Please enter a number.")