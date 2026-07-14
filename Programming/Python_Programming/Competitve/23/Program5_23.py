import os
import multiprocessing
import time
def Factorial(N):
    print(f"ppid is {os.getppid()}")
    fact=1
    for i in range(1,N+1):
        fact=fact*i
        
    print("Process ID is  :",os.getpid())
    print("Input Number :",N)
    print("Factorial",fact)


def main():
    print(f"PID is {os.getpid()} and ppid {os.getppid()}  of main")
    Data=[10,15,20,25]
    tobj1=multiprocessing.Pool()
    tobj1.map(Factorial,Data)
    tobj1.close()
    tobj1.join()






if __name__=="__main__":
    main()
