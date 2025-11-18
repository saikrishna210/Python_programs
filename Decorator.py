def helloworld1(func):
    def helloworld2():
        print("I am from Tanuku")
        func()
        print("I am 21 years Old")
    return helloworld2
@helloworld1
def say_hi():
    print("Krishna")
say_hi()