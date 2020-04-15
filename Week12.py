roster = ['Bob','Caleb','Michael','Morgan','Nick','Oscar','Pedro','Victor','William']

def student_check(roster):
    """
    This function prompts user for student name, compares input name with external list, and prints a statement based
    on if the name exist or not. Runs in While loop until user issues 'q'.
    :param roster:
    """
    student = None
    print("Welcome to the student checker!")
    while True:
        if student == None:
            student = input("Please give me the name of a student (enter 'q' to quit): ").title()
        elif student == 'Q':
            print("Goodbye!")
            break
        else:
            if student in roster:
                print("Yes, that student is enrolled in the class!")
                student = None
            else:
                print("No, that student is not in the class.")
                student = None

student_check(roster)