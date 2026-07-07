def CountSum(No):
    
     Sum=0
     while(No!=0):
         Digit=int(No%10)
         Sum=Sum+Digit
         No=int(No/10)
         
     return Sum


def main():
   Value1=int(input("Enter Number : "))
   Ret=CountSum(Value1)
   print(Ret)
   
if __name__=="__main__":
    main()