import threading
import time
def NumberS():
    Count=0
    current=threading.current_thread()
    for i in range(1,50+1,1):
        print(i,end=",")

    print(" ")
    print(f"The Captial Function Thread ID is",threading.get_ident(), f"And Name is {current.name}")

    print(" ")

      

def ReversePrint():
    Count=0
    Data=[]
    current=threading.current_thread()
    for i in range(50,0,-1):
        print(i,end=",")

    print(" ")
    print(f"The Small Function Thread ID is",threading.get_ident(), f"And Name is {current.name}")
    print(" ")





def main():
   
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=NumberS)
    tobj2=threading.Thread(target=ReversePrint)
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
  

    end_time=time.perf_counter()
    print(f"Time require is {end_time-start_time:.4f}")


if __name__=="__main__":
    main()
