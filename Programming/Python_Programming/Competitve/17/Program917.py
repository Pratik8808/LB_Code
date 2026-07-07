def CountDigit(No):
     Count=0
     while(No!=0):
         No=int(No/10)
         Count+=1
     return Count

         
         
     

      
  

      
    

def main():
   Value1=int(input("Enter Number"))
   Ret=CountDigit(Value1)
   print(Ret)
   
if __name__=="__main__":
    main()