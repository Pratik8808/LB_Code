
import os
import multiprocessing


def Mulof5(No):
    result=0
    for i in range(1,No+1):
        result=result+i**5
    return result


def main():
     print(f"PID of Main  is {os.getpid()} PPID of  main is :{os.getppid()}")
     Value1=int(input("Enter the number of elements :"))
     data=list()
     for i in range(1,Value1+1):
        temp=int(input(f"Enter number {i}th in list :"))
        data.append(temp)

if __name__=="__main__":
    main()