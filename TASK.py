a = int(input("Enter how many students are there: "))
b = []
for i in range(a):
    print("Enter the details of student")
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name of student: ")
    sub = input("Enter the subject: ")
    marks = int(input("Enter the marks: "))

    student = {"Roll no.": roll, "Name": name, "Subject": sub, "Marks": marks}
    b.append(student)

def dis(b):
    print("All Student Records:")
    for c in b:
        print(f"Roll No: {c['Roll no.']}, Name: {c['Name']}, "
              f"Subject: {c['Subject']}, Marks: {c['Marks']}")

def top(b):
    topper = max(b, key=lambda c: c["Marks"])
    print("Topper of the Class:")
    print(f"Roll No: {topper['Roll no.']}, Name: {topper['Name']}, "
          f"Subject: {topper['Subject']}, Marks: {topper['Marks']}")

def avg(b):
    total = sum(c["Marks"] for c in b)
    avg_marks = total / len(b)
    print("Class Average Marks:")
    print(f"Average Marks = {avg_marks:.2f}")

print("PRESS 1 TO GET DETAILS OF ALL STUDENTS")
print("PRESS 2 TO GET TOPPER STUDENT DETAILS")
print("PRESS 3 TO GET AVERAGE OF ALL STUDENTS")

d = int(input("Enter your choice: "))

if d == 1:
    dis(b)
elif d == 2:
    top(b)
elif d == 3:
    avg(b)
else:
    print("Enter valid number")

