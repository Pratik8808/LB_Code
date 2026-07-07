import threading
import time
def evenFactor(No):
    Data=[]
    for i in range(1,int(No/2)+1):
        if(No%i==0):
            Data.append(i)
    print(f"Even factor of the Number {Data}")

def OddFactor(No):
    Data=[]
    for i in range(1,int(No/2)+1):
        if(No%i!=0):
         Data.append(i)
    print(f" Odd Factor of the Number {Data}")

def main():
    Value=int(input("Enter the Number  to take input"))
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=evenFactor,args=[Value,])
    tobj2=threading.Thread(target=OddFactor,args=[Value,])

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    end_time=time.perf_counter()
    print(f"Time require is {end_time-start_time:.4f}")


if __name__=="__main__":
    main()
