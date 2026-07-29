
import sys
import os 
import datetime
def Display(Message):
    dictonary={}
    Name=os.path.join(Message)
    SubDriectoryCount=0
    FileNameCount=0
    ScanTime=datetime.datetime.now()
    if(os.path.exists(Message)):
        if(os.path.isdir(Message)):
         
            for FolderName ,Subdirectory,fileName in os.walk(Message):
              
                for subj in Subdirectory:
                    SubDriectoryCount=SubDriectoryCount+1
                for fname in fileName:
                    FileNameCount=FileNameCount+1


    print(f"Driectory Named  {Name}")
    print(f"Subdirectroy {SubDriectoryCount}")
    print(f"FileName  Count{FileNameCount}")

             
                


    

def main():
    if(len(sys.argv)==2):
        Display(sys.argv[1])
    else:
        print("Invaild Arugments")

    
if __name__=="__main__":
    main()