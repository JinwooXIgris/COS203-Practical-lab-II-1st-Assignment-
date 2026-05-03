# MAIN MODULE: Entry point — coordinates all other modules

import Input_module
import Logic_module
import Output_module


def main():
    # Step 1: Get input
    score = Input_module.get_score()

    # Step 2: Validate
    if not Logic_module.is_valid_score(score):
        Output_module.display_error("Score must be between 0 and 100.")
        return

    # Step 3: Compute grade and remarks
    grade = Logic_module.compute_grade(score)
    remarks = Logic_module.get_remarks(grade)

    # Step 4: Display result
    Output_module.display_result(score, grade, remarks)


if __name__ == "__main__":
    main()