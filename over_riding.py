class vehicle:
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started with ignition")
class bike(vehicle):
    def start(self):
        print("bike started with using key")
c1=vehicle()
c1.start()
d1=car()
d1.start()
