def printX(No):
    for i in range(1,No+1):
        for i in range(1,No+1):
            print("*",end=" ")
        print()

      
      
  
  
    
   
      
    

def main():
   Value1=int(input("Enter Number to print Pattern"))
   
   printX(Value1)
   
if __name__=="__main__":
    main()