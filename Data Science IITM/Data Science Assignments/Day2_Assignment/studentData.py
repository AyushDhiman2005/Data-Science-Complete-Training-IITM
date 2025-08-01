students = []

def addStudent(**kwargs):
    students.append(kwargs)

# Add students
addStudent(name="Alice", age=20, grade="A", id=101)
addStudent(name="Bob", age=22, grade="B", id=102)
addStudent(name="Charlie", age=21, grade="A+", id=103)



# Display students
for student in students:
    print(student)
