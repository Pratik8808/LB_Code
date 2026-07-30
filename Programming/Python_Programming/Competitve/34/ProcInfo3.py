import psutil
import os 
import schedule
import sys
import time
from writeSystemlog import systemLog

def LogActivity(DirectoryName):
    if(os.path.exists(DirectoryName)):
       print("Folder is Present")
    else:
        os.mkdir(DirectoryName)
        print("Driectory Created Sucessfully")
    filePath=os.path.join(DirectoryName,"LogFile.txt")
    systemLog(filePath)

       

        
           

# def WriteSystemLog(filePath):
#     if(len(sys.argv)==2):

#         listprocess=[]
#         for proc in psutil.process_iter():
#             info=proc.as_dict(attrs=["pid","name","username"])


#             listprocess.append(info)
#         fobj=(filePath,"a+")
    
   
       

def main():
    Border="-"*50
    if(len(sys.argv)==2):
        print(Border)
        print("Start of Script")
        print(Border)
        schedule.every(5).seconds.do(LogActivity,sys.argv[1])
    else:
        sys.exit()
    while True:
        schedule.run_pending()
        time.sleep(5)

    
    
if __name__=="__main__":
    main()