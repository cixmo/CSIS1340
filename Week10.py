name = None
grades = ["A","B","C","D","E","F"]
student_data = {}

while True:
    # Initializing name input and validation
    if name is None:
        name_input = input("Please give me the name of the student (q to quit): ").title()
        name = name_input
    elif name == 'Q':
        # Prints dictionary list in a readable table format and terminates the script.
        print("Okay, printing grades!\n")
        print("{:<22} {:1}".format('NAME', "GRADE"))
        for name, grade in student_data.items():
            print("{:<22} {:1}".format(name,grade))
        break
    # Checks name input against dictionary and gives user option to override current grade.
    elif name in student_data:
        print("A student named " + name + " with a grade of " + student_data[name] + " already exist in the database.")
        name_input = input("Do you wish to overwrite this record? (y or n): ")
        if name_input == 'y':
            del student_data[name]
            name_input = name
        else:
            name_input = input("Please give me the name of the student (q to quit): ").title()
    else:
        # User inputs grade; validation checks against grades list to see if grade is valid input.
        grade = input("Please give me their grade: ")
        grade = grade.upper()
        if grade in grades:
            student_data[name] = grade
            name = None
            del grade
        else:
            print("Grade is in a invalid format.\nValid Grades: A, B, C, D, E, F")