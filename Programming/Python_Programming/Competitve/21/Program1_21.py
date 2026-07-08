import threading
import time
def chkPrime(No):
    flag=True
    for i in range(1,(No/2)+1):
        if(No%i==0):
            flag=False
    return True

def Prime(No):
    Data=[]
    Ret=chkPrime(No)
    if(chkPrime==True):
        Data.append(No)
    

def main():
    Value=[10,233,442,53,65,12,54,77,31,346,73]
    


if __name__=="__main__":
    main()
