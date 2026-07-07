from functools import reduce
Morethan70=lambda no:(no>=70)
Map10=lambda no:no+10
Product=lambda no1,no2:no1*no2
def main():
   Data=[4,34,36,76,68,24,89,23,86,90,45,70]
   FData=list(filter(Morethan70,Data))
   print(FData)
   MData=list(map(Map10,FData))
   print(MData)
   RData=reduce(Product,MData)
   print(f"This is reduce data product {RData}")


  

if __name__=="__main__":
    main()
