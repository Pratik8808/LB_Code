def printX(No):
    for i in range(No,0,-1):
        for j in range(1,i+1,1):
            print("*",end=" ")
        print()

      
      
  
  
    
   
      
    

def main():
   Value1=int(input("Enter Number to print Pattern"))
   
   printX(Value1)
   
if __name__=="__main__":
    main()