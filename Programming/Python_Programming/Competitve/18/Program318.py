from functools import reduce
MinimumNumber=lambda No1,No2:(No2 if(No1>No2) else No1)

def main():
   Value=int(input("Enter number of elements"))
   Data=[]
   for i in range(1,Value+1):
       Value1=int(input(f"Enter {i} Element  :"))
       Data.append(Value1)
   Ret=reduce(MinimumNumber,Data)
   print(Ret)
if __name__=="__main__":
    main()
