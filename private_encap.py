# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
# e1=Employee("sai",40000)
# print("salary:",e1.__salary)

#public method to access private member
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def show(self):
        print("name:",self.name,"salary:",self.__salary)
e1=Employee("sai",40000)
e1.show()