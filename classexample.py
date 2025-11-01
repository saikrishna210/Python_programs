class employee:
    company_name="TCS"
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def show_company(self):
    # def show_company(self,new_name):
        # employee.company_name=new_name
        # print("updated company name:",employee.company_name)
        print("company_name:",employee.company_name)
e1=employee("sai","hyderabad")
# e2=employee("krishna","chennai")
print(e1.name)
e1.show_company()
# e1.show_company("wipro")
# print(e1.company_name)
# print(e2.company_name)



