import threading
import time
def Capital(str):
    Count=0
    current=threading.current_thread()
    Data=[]
    for i in str:
        if(i>='A' and i<='Z'):
            Count=Count+1
    print(f"Count of Capital Character is {Count}")
    print(f"The Captial Function Thread ID is",threading.get_ident(), f"And Name is {threading.current_thread().name}")

    print(" ")

      

def Small(str):
    Count=0
    Data=[]
    current=threading.current_thread()
    for i in str:
        if(i>='a' and i<='z'):
            Count=Count+1
    print(f" Count of Small Word is {Count}")

    print(f"The Small Function Thread ID is",threading.get_ident(), f"And Name is {current.name}")
    print(" ")


def Digits(str):
    Count=0
    current=threading.current_thread()

    for i in str:
        if(i>='0' and i<='9'):
            Count=Count+1
    print(f"Count of The Digit is {Count}")
    print(f"The Digit Function Thread ID is",threading.get_ident(), f"And Name is {current.name}")


def main():
    Value=input("Enter the String ")
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=Capital,args=(Value,))
    tobj2=threading.Thread(target=Small,args=(Value,))
    tobj3=threading.Thread(target=Digits,args=(Value,))

    tobj1.start()
    tobj2.start()
    tobj3.start()

    tobj1.join()
    tobj2.join()
    tobj3.join()
    end_time=time.perf_counter()
    print(f"Time require is {end_time-start_time:.4f}")


if __name__=="__main__":
    main()
