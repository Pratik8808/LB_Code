import threading
import time
def evenNumberSum(Arr):
    Sum=0
    Data=[]
    for i in Arr:
        if(i%2==0):
            Sum=Sum+i
            Data.append(i)
    print(f"Sum of Even Number is {Sum} and List is {Data}")

def OddNumberSum(Arr):
    Sum=0
    Data=[]
    for i in Arr:
        if(i%2!=0):
            Sum=Sum+i
            Data.append(i)
    print(f"Sum of Odd Number is {Sum} and List is {Data}")


def main():
    Value=[10,20,54,22,67,32,31,667,53]
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=evenNumberSum,args=(Value,))
    tobj2=threading.Thread(target=OddNumberSum,args=(Value,))

    tobj1.start()
    tobj2.start()

    end_time=time.perf_counter()
    print(f"Time require is {end_time-start_time:.4f}")


if __name__=="__main__":
    main()
