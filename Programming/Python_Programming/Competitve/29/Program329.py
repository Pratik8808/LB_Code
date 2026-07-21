import os
import sys
def FileCopied(DirectoryFile):
        
        print("Inside Demo txt")
        fobj=open("Demo.txt","+w")
        fobj.write("This text from Demo.txt will Copied in to Another File")
        sobj=open("Abc.txt","+a")
        fobj.seek(0)
        sobj.write(fobj.read())
        fobj.close()
        sobj.close()

        print("Sucesss in Copying File")



def main():
    if(len(sys.argv)==2):
         print("hiii")
         FileCopied(sys.argv[1])
    else:
         print(len(sys.argv))
         print("Invaild Command Line Arugmnent")

        
    
if __name__=="__main__":
    main()