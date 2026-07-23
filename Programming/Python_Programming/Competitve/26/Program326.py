class Demo:
    PI=3.14

    def __init__(self):
         self.Value1=0.0
         self.Value2=0.0
    def fun(self):
        print(self.Value1)
        print(self.no2)
    def Accept(self):
        self.Value1=int(input("Enter the first Number "))
        self.Value2=int(input("Enter the Second Number"))
    def Addition(self):
        return self.Value1+self.Value2
    def Subtraction(self):
        return self.Value2-self.Value1
    def Multiplication(self):
        return self.Value1*self.Value2
    def Divison(self):
        try:
            Result=self.Value1/self.Value2
            return Result

        except ZeroDivisionError as zobj:
            print("Divsion by Zero")
            return -1



def main():
    dobj=Demo()
    dobj.Accept()
    print(dobj.Addition())
    print(dobj.Divison())
    print(dobj.Multiplication())
    
    

if __name__=="__main__":
    main()   