

Even=lambda No1:(No1%2==0)
def main():
    Data=[2,3,5,6,8,10,12]
    Result=list(filter(Even,Data))
    print(len(Result))

if __name__=="__main__":
    main()