from functools import reduce


addition=lambda No1,No2:(No1+No2)
def main():
    Data=[2,3,4,5,6,7]
    Result=(reduce(addition,Data))
    print(Result)

if __name__=="__main__":
    main()