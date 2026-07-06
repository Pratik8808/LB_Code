def Divisibilty5(No1):
   if(No1%5==0):
      return True
   else:
      return False
     
   
      
    

def main():
   Value1=int(input("Enter First Number"))
   
   Result=Divisibilty5(Value1)
   print(f"{Result}") 
if __name__=="__main__":
    main()