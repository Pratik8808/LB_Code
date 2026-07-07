from functools import reduce 

Maximum=lambda No1,No2:(No1 if(No1>No2) else No2)
def MaximumNumber(Data):
    Result=reduce(Maximum,Data)
    return Result

    

def main():
    Data=[]
    Value=int(input("Enter how many Elements what to enter "))
    print("Enter the elements")
    for i in range(1,Value+1):
        Value1=int(input(f"Enter {i} Elmement :"))
        Data.append(Value1)
    Ret= MaximumNumber(Data)
    print(f"Maximum Number in List is {Ret}")


if __name__=="__main__":
    main()