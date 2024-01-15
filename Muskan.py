class Calculator:
    digit = 100  # variable immediate after class created call class variable

    def __init__(self,a,b):
        self.enter1 = a
        self.enter2 = b
        print("it's a constructor CALLED AUTOMATICALLY WHEN OBJECT IS Created")

    def Avnish(self):
        print("its a class program learning")


    def substraction(self):
        return self.enter1 + self.enter2 + Calculator.digit
    
    def NewGitub_code():
        num1 + num 2
        print("final output")



obj = Calculator(5,6)  # syntax to create objects
obj.Avnish()
print(obj.substraction())


obj1 = Calculator(4, 3)
obj1.Avnish()
print(obj1.substraction())


obj1 = Calculator(4, 3)
obj1.Avnish()
print(obj1.substraction())

