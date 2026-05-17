while True:

    try:
        marks = int(input("Enter marks: "))

        if marks > 100 or marks < 0:
            print("Please enter valid marks between 0 and 100.")

        elif marks >= 90:
            print("Grade: A")

        elif marks >= 75:
            print("Grade: B")

        elif marks >= 50:
            print("Grade: C")

        else:
            print("Grade: Fail")

    except ValueError:
        print("Please enter numbers only.")

    choice = input("Do you want to check again? (yes/no): ")

    if choice.lower() != "yes":
        print("Program ended.")
        break
