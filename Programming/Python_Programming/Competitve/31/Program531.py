import schedule
import datetime
import os
import sys

def CountFile(DirectoryName):
    count=0
    timestamp=datetime.datetime.now()
    if(os.path.exists(DirectoryName)):
        if(os.path.isdir(DirectoryName)):
            for FolderName,SubDirectory, FileName in os.walk(DirectoryName):
                count=len(FileName)
            fobj=open("MarvellOus.txt","a+")
            fobj.write("--------------------------------\n")
            fobj.write(DirectoryName+"\n")
            fobj.write(f"Number of Files : {count}\n")
            fobj.write(f"{timestamp}\n")

            fobj.close()

            print("Sucesss file is created")


        else:
            print(f"{DirectoryName} is not Directory")


    else:
        print("Unable Print to find Directory")



            
            
def main():
    if(len(sys.argv)==2):
        CountFile(sys.argv[1])

if __name__=="__main__":
    main()