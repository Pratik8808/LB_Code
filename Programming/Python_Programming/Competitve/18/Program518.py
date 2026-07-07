def chkPrime(no):
    
        
    flag=True

    if(no<=0):
        flag=Fal
    for i in range(2,int(no/2)+1):
        if(no%i==0):
            flag=False
            break
        
    return flag

def PrimeNumberSum(Arr):
    Sum=0
    for i in Arr:

        ret=chkPrime(i)
        if(ret==True):
            Sum=Sum+i
        else:
            continue
    return Sum


def main():
   Value=int(input("Enter number of elements"))
   Data=[]
   for i in range(1,Value+1):
       Value1=int(input(f"Enter {i} Element  :"))
       Data.append(Value1)
  
   Ret=PrimeNumberSum(Data)
   print(Ret)
if __name__=="__main__":
    main()
