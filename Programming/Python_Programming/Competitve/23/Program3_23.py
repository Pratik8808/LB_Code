import os
import multiprocessing
import time
def EvenNumber(N):
    print(f"ppid is {os.getppid()}")
    sum=0
    count=0
    for i in range(2,N+1):
        if(i%2==0):
            count+=1
            sum=sum+i
    print("Process ID is  :",os.getpid())
    print("Input Number :",N)
    print("Count of Even Number is",count)


def main():
    print(f"PID is {os.getpid()} and ppid{os.getppid()}  of main")
    Data=[100000,2000,30000,400000]
    tobj1=multiprocessing.Pool()
    tobj1.map(EvenNumber,Data)
    tobj1.close()
    tobj1.join()






if __name__=="__main__":
    main()
