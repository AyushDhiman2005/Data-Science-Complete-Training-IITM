class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_number=roll_no
        self.marks=marks
        print("Object Created Successfully!")

    def calculate_Grade(self):
        m = self.marks
        g=''
        if m>=85 and m<=100:
            g='A+'
        elif m>=65 and m<85:
            g='A'
        elif m>=50 and m<65:
            g='B+'
        elif m>33 and m<50:
            g='C'
        elif m<33:
            g='F'
        else:
            g='Grade Does not exists'
        f=open(f'{self.name}_recod.txt','w')
        f.write(f"Name: {self.name}\n")
        f.write(f"Roll Number: {self.roll_number}\n")
        f.write(f"Grade: {g}\n")
        f.close()
        print("Data Inserted Successfully!")
    
ayush=Student('ayush dhiman',108922,82)
ayush.calculate_Grade()