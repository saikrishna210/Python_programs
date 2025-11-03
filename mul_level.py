class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def vehicleinfo(self):
        print(f"brand:{self.brand},model:{self.model}")


class car(vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
    def carinfo(self):
        print(f"fuel_type:{self.fuel_type}")


class Electriccar(car):
    def __init__(self,brand,model,battery_capacity,fuel_type):
        super().__init__(brand,model,fuel_type)
        self.battery_capacity=battery_capacity
    def Electriccarinfo(self):
        print(f"battery_capacity:{self.battery_capacity}")
    
e1=Electriccar("TATA","SAFARI",40,"cng")
e1.vehicleinfo()
e1.carinfo()
e1.Electriccarinfo()