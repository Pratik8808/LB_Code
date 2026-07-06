def chkNumber(No):
    if(No%2==0):
        return 1
    else:
        return 0
    

def main():
   Value=int(input("Enter the Number to Check odd or not :  "))
   Result=chkNumber(Value)
   if(Result==1):
       print("Even Number")
   else:
       print("Odd Number")

if __name__=="__main__":
    main()