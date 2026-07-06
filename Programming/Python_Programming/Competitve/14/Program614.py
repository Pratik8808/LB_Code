OddNumber=lambda No1:(True if No1%2!=0 else False)

def main():
    Data=[2,3,4,5,6,7]
    Result=list(map(OddNumber,Data))
    print(Result)

if __name__=="__main__":
    main()