class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("name:",self.name,"salary:",self.salary)
e1=Employee("Sai",45000)
# print("name:",e1.name,"salary:",e1.salary)
e1.show()