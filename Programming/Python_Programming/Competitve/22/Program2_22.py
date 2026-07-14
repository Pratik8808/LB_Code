import time
from multiprocessing import Pool
import os

def Factorial(N):
        fact=1
        print(f"PID of Factorial:{os.getpid()} PPID of Factorail:{os.getppid()}")
        for i in range(1,N+1):
            fact=fact*i
        return fact

def main():
        print(f"PID of Main  is {os.getpid()} PPID of  main is :{os.getppid()}")
        Value1=int(input("Enter the number of elements :"))
        data=list()
        for i in range(1,Value1+1):
            temp=int(input(f"Enter number {i}th in list :"))
            data.append(temp)
        start_time=time.perf_counter()
        with Pool(processes=6)as pool:
            result=pool.map(Factorial,data)
            
        print(result)
        


        end_time=time.perf_counter()
        print(f"Total Time is {end_time-start_time} seconds :")

if __name__=="__main__":
        main()