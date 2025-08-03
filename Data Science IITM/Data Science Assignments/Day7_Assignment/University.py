
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Name : {name}\nAge : {age}")

class Student(Person):
    def __init__(self, name, age,id,course):
        super().__init__(name, age)
        self.student_id=id
        self.student_Course=course
        print(f"Student ID: {self.student_id}\nCourse: {self.student_Course}")
class Teacher(Person):
    def __init__(self, name, age,id,sub):
        super().__init__(name, age)
        self.employee_ID=id
        self.employee_Subject=sub
        print(f"Employee ID: {self.employee_ID}\nSubject :{self.employee_Subject}")
class TechStudent(Student):
    def __init__(self, name, age, id, course,programming_language):
        super().__init__(name, age, id, course)
        self.programming_Language=programming_language
        print(f"Programming Language: {self.programming_Language}")
print("_"*40)
person1 = Person('John',21)
print("_"*40)
Student1= Student('Michael',19,102033,'BCA')
print("_"*40)
teacher1= Teacher('Dr. ABC',45,113344,'Computer Networks')
print("_"*40)
TechStudent123= TechStudent('John',23,112233,'BCA','C++')
print("_"*40)