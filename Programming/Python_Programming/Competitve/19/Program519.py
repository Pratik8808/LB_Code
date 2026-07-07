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
        



MapSquare=lambda no:no*no
Addition=lambda no1,no2:no1+no2
def main():
   Data=[5,2,3,4,3,4,1,2,8,10]
   FData=PrimeorNot(Data)
   print(FData)
   MData=list(map(MapSquare,FData))
   print(MData)
   RData=reduce(Addition,MData)
   print(f"This is reduce function Addtion {RData}")


  

if __name__=="__main__":
    main()
