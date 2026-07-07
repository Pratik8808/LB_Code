def FactorsAddtion(No):
     sum=0
     for i in range(1,int(No/2)+1):
         if(No%i==0):
             sum+=i
     return sum
         
         
     

      
  
  
    
   
      
    

def main():
   Value1=int(input("Enter Number"))
   
   Ret= FactorsAddtion(Value1)

   print(f"Result of Factorial is {Ret}")
   
if __name__=="__main__":
    main()