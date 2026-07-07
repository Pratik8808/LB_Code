import time
import  threading

def Even():
    Count=0
    i=2
    Data=[]
    while(Count!=10):
        if (i%2==0):
            Count=Count+1
            Data.append(i)
        i=i+1
    print(Data)

def Odd():
    Count=0
    i=2
    Data=[]
    while(Count!=10):
        if (i%2!=0):
            Count=Count+1
            Data.append(i)
        i=i+1
    print(Data)

def main():
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=Even)
    tobj2=threading.Thread(target=Odd)
    tobj1.start()
    tobj2.start()
    tobj1.join()
    tobj2.join()
    end_time=time.perf_counter()

    print(f"The Time requrired is {end_time-start_time} Seconds")
    

if __name__=="__main__":
    main()
 
