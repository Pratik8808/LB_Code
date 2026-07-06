from functools import reduce

length5=lambda  str:(len(str)>5)
Minimum=lambda No1,No2:(No1 if No1<No2 else No2)
def main():
    Data=["AAA","CCCCCC","GGGSGSGS","AAA","FFFAW"]
    Result=list(filter(length5,Data))
    print(Result)

if __name__=="__main__":
    main()