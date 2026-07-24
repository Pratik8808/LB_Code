import sys
import schedule
import os
import time
Border="-"*40
def Display():
    print("Jay Ganesh ...")
    print(Border)
def main():
   
    print(Border)
 
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()