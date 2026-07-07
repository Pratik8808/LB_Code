def factorial(No):
     Fact=1
     for i in range(1,No+1):
      Fact=Fact*i
     return Fact

      
  
  
    
   
      
    

def main():
   Value1=int(input("Enter Number"))
   
   Ret= factorial(Value1)

   print(f"Result of Factorial is {Ret}")
   
if __name__=="__main__":
    main()