class company:
    def __init__(self):
        self._project="NLP"
class employee(company):
    def __init__(self,name):
        self.name=name
        company.__init__(self)
    def show(self):
        print("Employee name:",self.name)
        print("working on project:",self._project)
c1=employee("krishna")
c1.show()
print("project:",c1._project)