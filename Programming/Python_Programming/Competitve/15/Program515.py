from functools import reduce


Maximum=lambda No1,No2:(No1 if No1>No2 else No2)
def main():
    Data=[2,3,4,5,6,7]
    Result=(reduce(Maximum,Data))
    print(Result)

if __name__=="__main__":
    main()