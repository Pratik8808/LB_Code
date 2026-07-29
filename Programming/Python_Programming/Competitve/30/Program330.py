
import schedule
import time
import datetime
Border="-"*40
def Display():
    
    print("Coding kar ")
def main():
   
    print(Border)
    
    schedule.every(30).minutes.do(Display,Message=)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()