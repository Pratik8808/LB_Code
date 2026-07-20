import sys
import os
def FileReader(DirectoryPath):
   print(DirectoryPath,"This file of the syst")
   
   for FolderName,subFolder,FileName in os.walk("Test"):
        for fname in FileName:
            if(fname==DirectoryPath):
            #    print("Inside the if")
                fname=os.path.join(FolderName,fname)
              
                fobj=open(fname)
                Data=fobj.read()
                print(Data)
                fobj.close()
  
    
def main():
    if(len(sys.argv)==2):
        FileReader(sys.argv[1])
    else:
        print("Please enter Correct System Arugment")

if __name__=="__main__":
    main()