#student Eligiblity Checker
#program 2

# Read marks, attendance and project completion status
marks = int(input())
attendance = int(input())
project_status = input()

# Check the academic requirements
if marks >= 60 and attendance >= 75:
    # Check the project completion status
    if project_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")


# program 1
# whether the number is positive
# Read the number
number = int(input())

# Check whether the number is positive, negative or zero
if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")