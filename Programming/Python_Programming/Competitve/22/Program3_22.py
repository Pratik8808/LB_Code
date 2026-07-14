import math
from multiprocessing import Pool
import os

def CountP(No):
        prime=True
        print(f"PID of CountP : {os.getpid()} CountP  PPID : {os.getppid()}")

        for j in range(2, int(math.sqrt(No)) + 1):
            if No % j == 0:
                prime = False
                break
        return prime

def CountPrime(N):
    print(f"CountPrime PID : {os.getpid()}  CountPrime PPID : {os.getppid()}")

    count = 0

    for i in range(2, N + 1):
        prime = True

        prime=CountP(i)

        if prime:
            count += 1

    return count

def main():

    n = int(input("Enter number of elements : "))

    data = []

    for i in range(n):
        value = int(input("Enter number : "))
        data.append(value)

    with Pool(processes=4) as pool:
        result = pool.map(CountPrime, data)

    print("\nPrime Counts")

    for number, count in zip(data, result):
        print(f"1 to {number} = {count}")

if __name__ == "__main__":
    main()