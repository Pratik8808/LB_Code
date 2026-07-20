import os
def toFind(fileName):
    if os.path.exists(fileName):
        fobj=open(fileName,"r")
        
        for i in fobj:
            
            if("Marvellous" in i):
                print("Found the Letter Marvellous")
                break

    fobj.close()
         
                
         

   
def main():
    toFind("Demo.txt")
if __name__=="__main__":
    main()