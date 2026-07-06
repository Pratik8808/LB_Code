from functools import reduce

DivsibilityTest=lambda  No1:(No1%5==0 and No1 %3 ==0)

def main():
    Data=[2,3,4,5,6,7,8,9,15]
    Result=list(filter(DivsibilityTest,Data))
    print(Result)

if __name__=="__main__":
    main()