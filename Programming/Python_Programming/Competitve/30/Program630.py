import schedule
import time
import datetime
Border="-"*40
def Display():
    print("Lauch Time ! Every Day at 1:00PM ")

def WrapUp():
     print("Warp up Work EveryDay day at 6:00")



def main():
   
    print(Border)
    
    schedule.every().day.at("13:00").do(Display)
    schedule.every().day.at("18:00").do(WrapUp)
    while True:
        schedule.run_pending()
        time.sleep(45)
if __name__=="__main__":
    main()