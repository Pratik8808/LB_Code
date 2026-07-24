
import schedule
import time
import datetime
Border="-"*40
def Display():
    timeStamp=datetime.datetime.now()
    print("Current Time and Date :",timeStamp)
def main():
   
    print(Border)
    
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()