import os
import multiprocessing
import time
def SumOddd(N):
    print(f"Proces id  is  {os.getpid()}and  ppid is {os.getppid()}")
    sum=0
    for i in range(2,N+1):
        if(i%2==0):
            sum=sum+i
    return sum

def main():
    print(f"PID is {os.getpid()} and ppid{os.getppid()}  of main")
    Data=[100000,2000,30000,400000]
    tobj1=multiprocessing.Pool()
    result=tobj1.map(SumOddd,Data)
    tobj1.close()
    tobj1.join()

    print(result)





if __name__=="__main__":
    main()
