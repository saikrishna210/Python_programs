class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"name:{self.name},age:{self.age}")

class company:
    def __init__(self,company_name,location):
        self.company_name=company_name
        self.location=location
        print(f"company_name:{self.company_name},location:{self.location}")

class employee(person,company):
    def __init__(self,name,age,company_name,location,emp_name,emp_id):
        person.__init__(self,name,age)
        company.__init__(self,company_name,location)
        self.emp_name=emp_name
        self.emp_id=emp_id
        print(f"emp_name:{self.emp_name},emp_id:{self.emp_id}")
e1=employee("sai",20,"wipro","hyderabad","chudnru",90)
