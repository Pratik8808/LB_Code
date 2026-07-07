from functools import reduce
FilterEvenOut=lambda no:(no%2==0)
MapSquare=lambda no:no*no
Addition=lambda no1,no2:no1+no2
def main():
   Data=[5,2,3,4,3,4,1,2,8,10]
   FData=list(filter(FilterEvenOut,Data))
   print(FData)
   MData=list(map(MapSquare,FData))
   print(MData)
   RData=reduce(Addition,MData)
   print(f"This is reduce function Addtion {RData}")


  

if __name__=="__main__":
    main()
