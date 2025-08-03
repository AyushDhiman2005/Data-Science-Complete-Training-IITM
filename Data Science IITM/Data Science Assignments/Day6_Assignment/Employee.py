

class Employee():
    
    def __init__(self,person_Name, person_Salary, person_Department):
        self.__Name=person_Name
        self.__salary=person_Salary
        self.__department=person_Department

    def get_Details(self):
        print(f"\n{'_'*23}Person Details{'_'*23}\n|Name = {self.__Name} \n|Salary = {self.__salary} \n|Department = {self.__department}\n|{'_'*60}\n")
    def increase_salary(self,percentage):
        current_salary=self.__salary
        to_increase = current_salary * percentage / 100
        self.__salary=self.__salary+to_increase
        print(f"Salary Incremented from {current_salary} to {self.__salary} | @{percentage}% |")

john = Employee("John",50000,"Marketing Department")
john.get_Details()
john.increase_salary(14.3)
john.get_Details()
