import os
def Copied(fileName):
    if(os.path.exists(fileName)):
        fobj=open(fileName,"a")

        cobj=open("Abc.txt","w+")
        cobj.write("This the Test file  copied from abc.txt to demo")
        cobj.seek(0)
        Data= cobj.read()
        print(Data)
        fobj.write("\n"+Data)
        fobj.close()
        cobj.close()
       
       
        print("Sucessss")
    else:
        print("File not Exist")

def main():
    Copied("Demo.txt")
if __name__=="__main__":
    main()