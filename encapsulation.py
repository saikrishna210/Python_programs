class Employee:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project
    def show(self):
        print("Name:",self.name,"salary:",self.salary)
    def work(self):
        print(self.name,"is working on",self.project)
e1=Employee("sai",45000,"PYTHON")
e1.show()
e1.work()