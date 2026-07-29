import schedule
import time
import datetime
def display(Message):
    timestamp=datetime.datetime.now()
    print(timestamp)
    try:
        fobj=open("Marvellous.txt","a+")
        fobj.write(f"{timestamp}+\n")

        

    except Exception as eobj:
        print("Unable to Open files")
        

def main():
    Message=input("Enter Message")
    schedule.every(10).minutes.do(display,Message=Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

    
if __name__=="__main__":
    main()