import schedule
import os
import datetime
import sys
import shutil

def DriectoryCopy(SourcePath, CopyPath):
    if(os.path.isdir(SourcePath) and (os.path.isdir(CopyPath))):
      for folder,Subfolder ,filename in os.walk(SourcePath):
         for fname in filename:
            fobj=open("Marevellous.txt","a+")
            fobj.write(fname+"\n")
         




    shutil.copytree(SourcePath,CopyPath,dirs_exist_ok=True)
    print("SUcesss")



    
Border="-"*40
def Display():
    print("Lauch Time ! Every Day at 1:00PM ")

def WrapUp():
     print("Warp up Work EveryDay day at 6:00")



def main():
   if(len(sys.argv)==3):
       DriectoryCopy(sys.argv[1],sys.argv[2])
   else:
       print("Invaild Arugment in CLI")
       print(len(sys.argv))
       
      
       

    
if __name__=="__main__":
    main()