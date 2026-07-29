import datetime
import os
import schedule
import sys
def Size(Directory):
    now = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    if(os.path.isfile(Directory)):
        size=os.path.getsize(Directory)
        fobj=open("FileSizeLog.txt","+a")
        fobj.write(f"File Path : {Directory}\n")
        fobj.write(f"File Size : {size} bytes\n")
        fobj.write(f"Date & Time : {now}\n")
        fobj.write("--------------------------------------\n")
    else:
        print("File is under Creation")
        print("File is Created  Sucessfully")
        fobj=open("FileSizeLog.txt", "a")
        fobj.write(f"File Path : {Directory}\n")
        fobj.write("File does not exist.\n")
        fobj.write(f"Date & Time : {now}\n")
        fobj.write("--------------------------------------\n")

    
        


def main():
   if(len(sys.argv)==2):
       
        schedule.every(1).minutes.do(Size,Directory=sys.argv[1])
   else:
       print("InVaild Arugement")
   while True:
        schedule.run_pending()
if __name__=="__main__":
    main()