def FrequencyNumber(Arr,No):
    Count=0
    for i in Arr:
        if(i==No):
            Count=Count+1
    return Count


def main():
   Value=int(input("Enter number of elements"))
   Data=[]
   for i in range(1,Value+1):
       Value1=int(input(f"Enter {i} Element  :"))
       Data.append(Value1)
   Value1=int(input("Enter Number to serach"))
   Ret=FrequencyNumber(Data,Value1)
   print(Ret)
if __name__=="__main__":
    main()
