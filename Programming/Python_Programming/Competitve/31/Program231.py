import schedule
import time
def display(Message):
    
    print(Message)

def main():
    Message=input("Enter Message")
    schedule.every(5).seconds.do(display,Message=Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

    
if __name__=="__main__":
    main()