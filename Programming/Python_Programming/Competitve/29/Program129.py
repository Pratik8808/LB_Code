import os
def CheckFileDirectory(file,serachfile):
    Ret=False
    for folderName,subFolder,Filename in os.walk(file):
        for fname in Filename:
            print(Filename)
            if(fname ==serachfile):
                Ret=True
                break
    return Ret

def main():     
    Ret=CheckFileDirectory("Test","Abc.txt")
    if(Ret==True):
        print("File is Present in Directory")
    else:
        print("File is Not Present")
if __name__=="__main__":
    main()