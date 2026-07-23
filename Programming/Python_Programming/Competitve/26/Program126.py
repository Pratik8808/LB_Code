class Demo:
    Value=0

    def __init__(self,Value1,Value2):
         self.no1=Value1
         self.no2=Value2
    def fun(self):
        print(self.no1)
        print(self.no2)
    def gun(self):
        print(self.no1)
        print(self.no2)

def main():
    dobj=Demo(11,21)
    doj1=Demo(51,101)
    dobj.fun()
    dobj.gun()
    doj1.fun()
    doj1.gun()

if __name__=="__main__":
    main()   