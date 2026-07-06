def chkNumber(No1):
   if(No1>0):
      return "Positive Number"
   elif(No1<0):
      return "Negative Number"
   else:
      return  "Zero"
      
    

def main():
   Value1=int(input("Enter First Number"))
   
   Result=chkNumber(Value1)
   print(f"{Result}")   
if __name__=="__main__":
    main()