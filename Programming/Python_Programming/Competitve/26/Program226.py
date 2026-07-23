class Demo:
    PI=3.14

    def __init__(self):
         self.no1=0
    def fun(self):
        print(self.no1)
        print(self.no2)
    def Accept(self):
        self.no1=int(input("Enter the Number "))
    def CalculateArea(self):
        return self.no1*self.no1*Demo.PI
    def CalculateCircumference(self):
        return 2*self.no1*Demo.PI



def main():
    dobj=Demo()
    dobj.Accept()
    Ret=dobj.CalculateArea()
    print(Ret)
    Ret=dobj.CalculateCircumference()
    print(Ret,"CalculateCircumference")
    
    

if __name__=="__main__":
    main()   