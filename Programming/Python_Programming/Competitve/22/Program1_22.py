import time
from multiprocessing import Pool
def square  (Number):
    return  Number*Number

def main():
    Value1=int(input("Enter the number of elements :"))
    data=list()
    for i in range(1,Value1+1):
        temp=int(input(f"Enter number {i}th in list :"))
        data.append(temp)
    start_time=time.perf_counter()
    with Pool(processes=2) as pool:
        result=pool.map(square,data)
    
    print(result)


    end_time=time.perf_counter()
    print(f"Total Time is {end_time-start_time} seconds :")
if __name__=="__main__":
    main()