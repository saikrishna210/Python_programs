class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0
calc = Calculator()
print(calc.add())         
print(calc.add(5))        
print(calc.add(5, 10))     
print(calc.add(5, 10, 15)) 
