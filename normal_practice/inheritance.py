class Person():
    def __init__(self, name) -> None:
        print("You are in Person __init__")
        self.name = name
        
    def display(self):
        print("display: {}".format(self.name))
        

class Department(Person):
    def __init__(self, name, dep_id) -> None:
        print("You are in Department __init__") 
        super().__init__(name)
        self.dep_id = dep_id
    
    def department_id(self):
        print("department_id: {}".format(self.dep_id) )


        
class Employee(Department):
    def __init__(self, name, dep_id, emp_id) -> None:
        print("You are in Employee __init__")
        super().__init__(name, dep_id)
        self.emp_id = emp_id
        
    def employee_id(self):
        print("employee_id: {}".format(self.emp_id))
        
        
class Salary(Person):
    def __init__(self, name, salary) -> None:
        print("Your are in Salary __init__")
        super().__init__(name)
        
        # Department().__init__(self)
        self.salary = salary
        
    def salary_(self):
        print("salary: {}, {}".format(self.salary, self.name))
        
        
sal_obj = Salary("ats", 120000)
sal_obj.salary_()        
# emp_obj = Employee("ankit", 10, 41)
# emp_obj.display()
# emp_obj.department_id()
# emp_obj.employee_id()

