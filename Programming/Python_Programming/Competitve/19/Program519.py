Multiply2=lambda No:No*2
from functools import reduce
def ChkPrime(Number):
    flag=True
    for i in range (2,int(Number/2)+1):
        if(Number%i==0):
            flag=False
            break
    return flag


def PrimeorNot(No):
    Data=[]
    for i in No:
        Ret=ChkPrime(i)
        if(Ret==True):
            Data.append(i)
    
    return Data
        



MapSquare=lambda no:no*no
Addition=lambda no1,no2:no1+no2
Max=lambda no1,no2:(no1 if(no1>no2)else no2)
def main():
   Data=[2,70,11,10,17,23,31,77]
   FData=PrimeorNot(Data)
   print(FData)
   MData=list(map(Multiply2,FData))
   print(MData)
   RData=reduce(Max,MData)
   print(f"This is reduce function Addtion {RData}")


  

if __name__=="__main__":
    main()
