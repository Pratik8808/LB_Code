import datetime
import os
import schedule
def Time():
        timestamp=datetime.datetime.now()
        Date=datetime.datetime.now().strftime("%d-%m-%Y")
        fobj=open((f"file{timestamp}"),"a+")
        fobj.write(f"FileName -file{timestamp}")
        fobj.write(f"Creation Date: {datetime.datetime.now().strftime("%d-%m-%y")}")
        fobj.write(f"Creation Time :{datetime.datetime.now().strftime("%H:%M:%S")}")
        fobj.close()
        


def main():
   schedule.every(1).minutes.do(Time)
   while True:
        schedule.run_pending()
if __name__=="__main__":
    main()