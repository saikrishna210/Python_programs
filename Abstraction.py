from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class car(vehicle):
    def start(self):
        print("car started with key ignition")
    def stop(self):
        print("car stoped with breaking system")
c1=car()
c1.start()
c1.stop()
