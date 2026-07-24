
import schedule
import time
import datetime
Border="-"*40
def Display():
    
    print("Namaskar ")
def main():
   
    print(Border)
    
    schedule.every().day.at("9:00").do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()