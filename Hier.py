class Animal:
    def sound(self):
        print("Animals make different sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks:woof woof!")
class Cat(Animal):
    def sound(self):
        print("cat meows:meow meow!")
class Cow(Animal):
    def sound(self):
        print("cow Ambha:ambha ambha!")
d1=Dog()
d2=Cat()
d3=Cow()
d1.sound()
d2.sound()
d3.sound()
