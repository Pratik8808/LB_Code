square=lambda No:No*No

def main():
    Data=[2,3,4,5,6,7]
    Result=list(map(square,Data))
    print(Result)

if __name__=="__main__":
    main()