def SumList(Data):
    Sum=0
    for i in Data:
        Sum=i+Sum
    return Sum


def main():
    Data=[]
    Value=int(input("Enter how many Elements what to enter "))
    print("Enter the elements")
    for i in range(1,Value+1):
        Value1=int(input(f"Enter {i} Elmement :"))
        Data.append(Value1)
    Ret= SumList(Data)
    print(f"Addition of List is {Ret}")


if __name__=="__main__":
    main()