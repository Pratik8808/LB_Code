Squares=lambda No1:No1**2
def main():
    Data=[2,3,4,5,6,7]
    Result=list(map(Squares,Data))
    print(Result)

if __name__=="__main__":
    main()