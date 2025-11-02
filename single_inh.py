class company_name:
    company_name="tcs"
    def __init__(self):
        self.name="python"
        self.location="kerala"
    def show_details(self):
        print(f"name:{self.name},location:{self.location}")
        
class employee(company_name):
    def __init__(self,name,id):
        self.name=name
        self.id=id
        super().__init__()
e1=employee("sai",596)
e1.show_details()
print(e1.company_name)
print(e1.id)

