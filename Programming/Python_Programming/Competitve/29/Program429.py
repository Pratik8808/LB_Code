import os
import sys

def Countstr(Str):
     fobj=open("Demo.txt","r+")
     count=0
     for i in fobj:
         line=i.split()
         for j in line:
             if(j==Str):
                 count=count+1
        
       
     return count


def main():
    if(len(sys.argv)==2):

        Ret=Countstr(sys.argv[1])
        print(Ret)
   
if __name__=="__main__":
    main()