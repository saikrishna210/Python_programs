class Employee:
    company_name = "TCS"
    # Constructor (automatically called when object is created)
    def __init__(self,name,location,salary):
        self.name = name
        self.location = location  
        self.salary = salary      
    def display_details(self):
        print("Employee Name:", self.name)
        print("Location:", self.location)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)
e1 = Employee("Sai Krishna", "Hyderabad", 50000)
e1.display_details()
