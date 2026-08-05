#program4
#for loops
# Read the number and word
n = int(input())
character = input()

# Print the number sequence
print("Numbers:")
for i in range(1,n+1):
    print(i)

print("Characters:")
for c in character:
    print(c)

#program3
#claculate total

# Read the value of n
n = int(input())

# Initialize the counter and total
counter = 1
total = 0

# Calculate the total using a while loop
while counter <= n:
    total = total + counter
    counter += 1

# Display the total
print(f"Total: {total}")




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