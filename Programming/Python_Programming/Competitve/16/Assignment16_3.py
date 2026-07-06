def Add(No1,No2):
   return(No1+No2)
    

def main():
   Value1=int(input("Enter First Number"))
   Value2=int(input("Enter the Second Number"))
   Result=Add(Value1,Value2)
   print(f"Addition of {Value1} & {Value2} : {Result}")   
if __name__=="__main__":
    main()