class Employee:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called: Object created for {self.name}")
    def __del__(self):
        print(f"Destructor called: Object deleted for {self.name}")
e1 = Employee("Sai")
del e1
print("Program is ending...")
