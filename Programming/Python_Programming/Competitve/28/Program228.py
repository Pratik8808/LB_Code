def main():
    robj=open("Demo.txt","r")
   
    Data=robj.read()
    Count=Data.split()
    print(Count)
   
if __name__=="__main__":
    main()


    
    
   
